from ..database.db import db
from sqlalchemy import Column, Integer, String, BIGINT, Float
class Position(db.Model):
    stockID = db.Column(Integer, primary_key=True)
    inPrice = db.Column(Float)
    charge = db.Column(Float)
    time = db.Column(BIGINT)
    owner = db.Column(db.String(100), primary_key=True)
    def __init__(self, userId, stockID):
        self.owner = userId
        self.stockID = stockID
        self.inPrice = 0
        self.charge = 0
        self.time = 0
    def isValid(self):
        if self.time ==0:
            return False
        return True
    def __repr__(self):
        return "<Position %r>" % self.stockID
