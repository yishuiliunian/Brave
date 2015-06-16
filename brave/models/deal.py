from ..database.db import db

class DealRecord(db.Model):
    identifier = db.Column(db.String(32), primary_key=True)
    stock = db.Column(db.String(100))

    def __init__(self, identifier, stock):
        self.identifier = identifier
        self.stock = stock

    def __repr__(self):
        return "<DealRecord>: %r" % self.stock
