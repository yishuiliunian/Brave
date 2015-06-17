from ..app.app import app
from ..app.app import api
from ..database.db import db
from ..businiss.deals.deals import DealRecordResource
from ..businiss.positions.position import PositionResource
def applicationWillLunch():
    app.config['DEFAULT_PARSERS'] = [
        'flask.ext.api.parsers.JSONParser'
    ]

    app.config['DEFAULT_RENDERERS'] = [
        'flask.ext.api.renderers.JSONRenderer',
    ]
    db.create_all()
    api.add_resource(DealRecordResource, "/test")
    api.add_resource(PositionResource, "/position")
    print "Begin Loading"
