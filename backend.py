from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CJ2938cj@119.8.60.213:23306/DemoServerDB'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World!'}


class Login(Resource):
    def get(self):
        return {'Hello': 'World!'}


class TestCase(Resource):
    def get(self):
        return {'Hello': 'World!'}


api.add_resource(HelloWorld, '/')
api.add_resource(Login, '/login')
api.add_resource(TestCase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
