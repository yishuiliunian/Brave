from ...database.db import db
from ...app.app import app
from ...models.deal import DealRecord
from flask_restful import Resource
from flask import Flask, request
from ...utils.response import BraveErrorResponse, BraveResponse


class PositionResource(Resource):
    def get(self):
        return BraveResponse({"a":request.args})
