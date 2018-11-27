import json
import cherrypy
from _citibike_database import _citibike_database

class ServiceController(object):
    def __init__(self, bdb = None):
        if bdb is None:
            self.bdb = _citibike_database()
        else:
            self.bdb = bdb

    def GET_SERVICE_SID(self, sid):
        sid = int(sid)
        output = {'result' : 'success'}
        try:
            res = self.bdb.get_service(sid)
            if res == 'error':
                output['result'] = 'error'
            else:
                output['value'] = res
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    def PUT_SERVICE_SID(self, sid):
        sid = int(sid)
        output = {'result' : 'success'}
        try:
            res = self.bdb.update_service(sid)
            if res == 'error':
                output['result'] = 'error'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
