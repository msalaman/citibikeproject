import cherrypy

from stations import StationsController
from close import CloseController
#from rent import RentController
#from park import ParkController
#from service import ServiceController

from _citibike_database import _citibike_database

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    bdb_o = _citibike_database()
    bdb_o.load_stations('bikeStations.dat')
    # instantiate controllers
    stationController = StationsController(bdb_o)
    closeController = CloseController(bdb_o)
    #rentController = RentController(bdb=bdb_o)
    #parkController =ParkController(bdb=bdb_o)
    #serviceController = ServiceController(bdb=bdb_o)

    # resources

    # /stations/ - GET, POST
    dispatcher.connect('get_station', '/stations/', controller=stationController, action='GET', conditions=dict(method=['GET']))
    dispatcher.connect('post_station', '/stations/', controller=stationController, action='POST', conditions=dict(method=['POST']))


    # /stations/:id - GET, DELETE
    dispatcher.connect('station_get', '/stations/:sid', controller=stationController, action='GET', conditions=dict(method=['GET']))
    dispatcher.connect('station_delete', '/stations/:sid', controller=stationController, action='DELETE', conditions=dict(method=['DELETE']))

    # /closest/ - POST
    dispatcher.connect('closest_post', '/closest/', controller=closeController, action='POST', conditions=dict(method=['POST']))
    # /rent/:id - PUT

    # /park/:id - PUT

    # /service/:id - GET, PUT


    # configuration for server
    conf = { 'global' : { 'server.socket_host' :'student04.cse.nd.edu', 'server.socket_port' : 52080 },
    '/' : { 'request.dispatch' : dispatcher }, }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()
