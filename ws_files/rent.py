import json
import cherrypy
from _citibike_database import _citibike_database

class RentController(object):
    def __init__(self, bdb = None):
        if bdb is None:
            self.bdb = _citibike_database()
        else:
            self.bdb = bdb

    def PUT_SID(self, sid):
        output = {'result' : 'success'}
        sid = int(sid)
        try:
            res = self.bdb.rent_bike(sid)
            if res == 'error':
                output['result'] = 'error'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
