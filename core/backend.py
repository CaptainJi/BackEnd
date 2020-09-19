from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# 配置数据库
'''
Python Console中输入如下命令创建表

from core.backend import db
db.create_all()
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@119.8.60.213:23306/DemoServerDB'
db = SQLAlchemy(app)


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


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World!'}


class LoginApi(Resource):
    def get(self):
        res = {}
        for i in User.query.all():
            res['id'] = i.id
            res['username'] = i.username
            res['email'] = i.email
        return res

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
    def get(self):
        res = {}
        for i in TestCase.query.all():
            res['id'] = i.id
            res['casename'] = i.casename
            res['description'] = i.description
            res['data'] = i.data
        return res

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

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(HelloWorld, '/')
api.add_resource(LoginApi, '/login')
api.add_resource(TestCaseApi, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
