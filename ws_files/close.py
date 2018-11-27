import cherrypy
import re, json
from _citibike_database import _citibike_database

class CloseController(object):
    def __init__(self, bdb = None):
        if bdb is None:
            self.bdb = _citibike_database()
        else:
            self.bdb = bdb

    def POST(self):
        output = {'result':'success'}
        data = json.loads(cherrypy.request.body.read())
        lat = data['latitude']
        lon = data['longitude']
        sid = self.bdb.get_closest_station(lat, lon)
        output['station_id'] = sid
        return json.dumps(output)
