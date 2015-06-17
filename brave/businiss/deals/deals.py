from ...database.db import db
from ...app.app import app
from ...models.deal import DealRecord
from flask_restful import Resource
from flask import Flask, request
from flask.ext.api.parsers import JSONParser
from flask.ext.api.decorators import set_parsers
from flask.ext.api.decorators import set_renderers
from flask.ext.api.renderers import JSONRenderer
from flask import jsonify

class DealRecordResource(Resource):
    def get(self):
        return {"a":"a"}
