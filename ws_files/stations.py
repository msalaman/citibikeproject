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

	# /stations/
	def GET_STATIONS(self):
		l = []
		for i in self.bdb:


			
			genreTitle = self.mdb.get_movie(i) # get genre and title for i [name, genres]
			temp = {}
			temp['genres'] = genreTitle[1]
			temp['title'] =  genreTitle[0]
			temp['id'] = i
			temp['img'] = self.get_poster_by_mid(int(i))
			l.append(temp)

		output = {'movies':l, 'result':'success'}
		return json.dumps(output)
