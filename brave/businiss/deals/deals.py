from ...database.db import db
from ...models.deal import DealRecord
from flask_restful import Resource
from flask import Flask, request
from ...utils.response import BraveErrorResponse, BraveResponse


class DealRecordResource(Resource):
    def get(self):
        return BraveResponse({"a":"a"})
