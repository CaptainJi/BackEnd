from flask_sqlalchemy import SQLAlchemy

from core.backend import app

# done:数据库操作
'''
Python Console中输入如下命令创建表

from handleDB import db
db.create_all()
'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@www.captainnas.com:23306/DemoServerDB'
db = SQLAlchemy(app)


# done:创建用户数据表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# done:创建测试用例数据表
class TestCase(db.Model):
    __tablename__ = 'testcase'
    id = db.Column(db.Integer, primary_key=True)
    casename = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(1024), unique=False, nullable=False)
    data = db.Column(db.String(1024), unique=False, nullable=False)

    def __repr__(self):
        return '<TestCase %r>' % self.casename


# done:创建任务数据表
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    # tasknumber = db.Column(db.String(20), unique=True, nullable=False)
    taskname = db.Column(db.String(80), unique=False, nullable=False)
    # description = db.Column(db.String(1024), unique=False, nullable=False)
    # tasktime = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.taskname
