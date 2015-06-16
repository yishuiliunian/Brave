from ...database.db import db
from ...app.app import app
from ...models.deal import DealRecord
from flask_restful import Resource
from flask import Flask, request


class DealRecordResource(Resource):
    def get(self, recordId):
        return "request is %r" % recordId
