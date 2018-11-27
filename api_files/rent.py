import json
import cherrypy
from _citibike_database import _citibike_database

class RentController(object):
    def __init__(self, bdb = None):
        
