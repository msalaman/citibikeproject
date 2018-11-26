import json
import requests
import cherrypy

from _citibike_database import _movie_database

class StationsController(object): 
	def __init(self, db=None):
		if db is None: 
			self.db = _citibike_database()
		else:
			self.db = db

		self.db.load_stations()
