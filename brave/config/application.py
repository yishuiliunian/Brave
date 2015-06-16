from ..app.app import app
from ..app.app import api
from ..database.db import db
from ..businiss.deals.deals import DealRecordResource

def applicationWillLunch():
    db.create_all()
    api.add_resource(DealRecordResource, "/xx/<string:recordId>")
    print "Begin Loading"
