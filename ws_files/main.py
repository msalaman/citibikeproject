import json
import cherrypy
from stations import StationsController
from close import CloseController
from rent import RentController
from park import ParkController
from service import ServiceController
from reset import ResetController

from _citibike_database import _citibike_database

class optionsController:
    def OPTIONS(self, *args, **kargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    bdb_o = _citibike_database()
    bdb_o.load_stations('bikeStations.dat')
    # instantiate controllers
    stationController = StationsController(bdb_o)
    closeController = CloseController(bdb_o)
    rentController = RentController(bdb=bdb_o)
    parkController = ParkController(bdb=bdb_o)
    serviceController = ServiceController(bdb=bdb_o)
    resetController = ResetController(bdb_o)
	# resources

    # /stations/ - GET, POST, DELETE
    dispatcher.connect('get_stations', '/stations/', controller=stationController, action='GET_STATIONS', conditions=dict(method=['GET']))
    dispatcher.connect('post_stations', '/stations/', controller=stationController, action='POST_STATIONS', conditions=dict(method=['POST']))
    dispatcher.connect('delete_stations', '/stations/', controller=stationController, action='DELETE_ALL', conditions=dict(method=['DELETE']))

    # /stations/:id - GET, DELETE
    dispatcher.connect('station_get', '/stations/:sid', controller=stationController, action='GET', conditions=dict(method=['GET']))
    dispatcher.connect('station_delete', '/stations/:sid', controller=stationController, action='DELETE', conditions=dict(method=['DELETE']))

    # /closest/ - POST
    dispatcher.connect('closest_post', '/closest/', controller=closeController, action='POST', conditions=dict(method=['POST']))

    # /rent/:id - PUT
    dispatcher.connect('rent_put', '/rent/:sid', controller=rentController, action='PUT_SID', conditions=dict(method=['PUT']))

    # /park/:id - PUT
    dispatcher.connect('park_put', '/park/:sid', controller=parkController, action='PUT_PARK_SID', conditions=dict(method=['PUT']))

    # /service/:id - GET, PUT
    dispatcher.connect('service_get', '/service/:sid', controller=serviceController, action='GET_SERVICE_SID', conditions=dict(method=['GET']))
    dispatcher.connect('service_put', '/service/:sid', controller=serviceController, action='PUT_SERVICE_SID', conditions=dict(method=['PUT']))

    # /reset/ - PUT
    dispatcher.connect('reset_put', '/reset/', controller=resetController, action='PUT', conditions=dict(method=['PUT']))

    dispatcher.connect('stations_options', '/stations/', controller=optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('station_id_options', '/stations/:sid', controller=optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('closest_options', '/closest/', controller=optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('rent_options', '/rent/:sid', controller=optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('park_options', '/park/:sid', controller=optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('service_options', '/service/:sid', controller=optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))


    # configuration for server
    conf = { 'global' : { 'server.socket_host' :'student04.cse.nd.edu', 'server.socket_port' : 52080 },
    '/' : { 'request.dispatch' : dispatcher,
            'tools.CORS.on' : True,
          }
            }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
