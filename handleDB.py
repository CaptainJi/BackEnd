from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# done:数据库操作
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CJ2938cj@119.8.60.213:23306/DemoServerDB'
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
    date = db.Column(db.String(1024), unique=False, nullable=False)

    def __repr__(self):
        return '<TestCase %r>' % self.casename
