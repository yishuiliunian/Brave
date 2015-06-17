from ...database.db import db
from ...app.app import app
from ...models.deal import DealRecord
from flask_restful import Resource
from flask import Flask, request
from ...utils.response import BraveErrorResponse, BraveResponse


@app.route("/position/add")
def AddPosition():
    return BraveResponse({"data", request.args})
