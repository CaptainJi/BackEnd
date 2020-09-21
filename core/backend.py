from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
# 配置json转ASCII编码已解决返回json中中文的UTF-8编码问题
app.config['JSON_AS_ASCII'] = False
api = Api(app)
jenkins = Jenkins('http://www.captainnas.com:28080', username='admin', password='110510b6c9f4b6ad083384608a0c3a3be9')

# 配置数据库
'''
Python Console中输入如下命令创建表

from core.backend import db
db.create_all()
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@127.0.0.1:23306/DemoServerDB'
db = SQLAlchemy(app)
# token管理
app.config['JWT_SECRET_KEY'] = 'TestPlatform'
jwt = JWTManager(app)


# done:用户数据表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# done:测试用例数据表
class TestCase(db.Model):
    __tablename__ = 'testcase'
    id = db.Column(db.Integer, primary_key=True)
    casename = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(1024), unique=False, nullable=False)
    data = db.Column(db.String(1024), unique=False, nullable=False)

    def __repr__(self):
        return '<TestCase %r>' % self.casename

# done:任务数据表
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(20), unique=True, nullable=False)
    # taskname = db.Column(db.String(80), unique=False, nullable=False)
    # description = db.Column(db.String(1024), unique=False, nullable=False)
    # tasktime = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.taskname

# 首页
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World!'}


# done:登录
class LoginApi(Resource):
    def get(self):
        return {'Hello': 'World!'}

    def post(self):
        # done: 查询数据库
        username = request.json.get('username', None)
        # todo: 通常密码不建议原文存储
        password = request.json.get('password', None)
        user = User.query.filter_by(username=username, password=password).first()
        # done: 生成返回结构体
        if user is None:
            # 使用jsonify传回json体,输出中文
            return jsonify(
                errcode=1,
                errmsg='用户名或密码错'
            )
        else:
            # done: 生成token
            return {
                'errcode': 0,
                'errmsg': 'ok',
                'username': user.username,
                'token': create_access_token(identity=user.username)
            }


# done: 注册用户
class RegisterApi(Resource):
    def post(self):
        t = User(username=request.json['username'],
                 password=request.json['password'],
                 email=request.json['email'])
        db.session.add(t)
        db.session.commit()
        return {
            'msg': 'ok'
        }


class TestCaseApi(Resource):
    @jwt_required
    def get(self):
        r = []
        for i in TestCase.query.all():
            res = {}
            res['id'] = i.id
            res['casename'] = i.casename
            res['description'] = i.description
            res['data'] = i.data
            r.append(res)
        return r

    @jwt_required
    def post(self):
        '''
        测试命令:curl http://127.0.0.1:5000/testcase -d '{"casename":"testdemo","description":"test description","data":"test data"}' -H 'content-type: application/json
        :return:
        '''
        t = TestCase(casename=request.json['casename'],
                     description=request.json['description'],
                     data=request.json['data'])
        db.session.add(t)
        db.session.commit()
        return {
            'msg': 'ok'
        }

    # done:更新用例
    @jwt_required
    def put(self):
        casename = request.json.get('casename', None)
        description = request.json.get('description', None)
        update_casename = request.json.get('update_casename', None)
        update_description = request.json.get('update_description', None)
        update_data = request.json.get('update_data', None)

        t = TestCase.query.filter_by(casename=casename, description=description).first()
        if t is None:
            return jsonify(
                errcode=1,
                errmsg='用例不存在')
        else:
            t.casename = update_casename
            t.description = update_description
            t.data = update_data
            db.session.commit()
            return {
                'msg': 'update success'
            }

    # done：删除用例
    @jwt_required
    def delete(self):
        casename = request.json.get('casename', None)
        description = request.json.get('description', None)
        t = TestCase.query.filter_by(casename=casename, description=description).first()
        if t is None:
            return jsonify(
                errcode=1,
                errmsg='用例不存在')
        else:
            db.session.delete(t)
            db.session.commit()
            return {
                'msg': 'delete success'
            }


# done:调度jenkins
class TaskApi(Resource):
    # @jwt_required
    #done:查询所有任务
    def get(self):
        r = []
        for i in Task.query.all():
            res = {}
            res['taskname'] = i.taskname
            r.append(res)
        return r

    @jwt_required
    def post(self):
        # done:用例获取
        testcases = request.json.get('testcases', None)
        jenkins['testcase'].invoke(securitytoken='110510b6c9f4b6ad083384608a0c3a3be9', build_params={
            'testcases': testcases
        })
        # dome:任务添加入数据库
        t = Task(taskname=jenkins['testcase'].get_last_completed_build().get_number()
        )
        print(t)
        db.session.add(t)
        db.session.commit()
        return {
            'errcode': 0,
            'errmsg': 'ok'
        }
        # todo:结果交给其它接口异步处理


api.add_resource(HelloWorld, '/')
api.add_resource(LoginApi, '/login')
api.add_resource(TestCaseApi, '/testcase')
api.add_resource(RegisterApi, '/register')
api.add_resource(TaskApi, '/task')

if __name__ == '__main__':
    app.run(debug=True)
