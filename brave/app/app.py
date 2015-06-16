from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

class HelloWorld(Resource):
    def get(self):
        return {"hello":'world'}


api.add_resource(HelloWorld, "/")
