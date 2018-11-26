import json
import requests
import cherrypy

from _citibike_database import _citibike_database

class StationsController(object):
	def __init__(self, bdb=None):
		if bdb is None:
			self.bdb = _citibike_database()
		else:
			self.bdb = bdb

		self.bdb.load_stations('bikeStations.dat')
