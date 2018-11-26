import json
import requests
import cherrypy

from _citibike_database import _citibike_database


class StationsController(object): 
	def __init__(self, bdb):
		self.bdb=bdb

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

	# /stations/:id

	def GET(self, sid):
		output = {'result':'success'}
		sid = int(sid)
		station = self.bdb.get_station(sid)
		if station != 'error':
			output['stationName'] = station['stationName']
			output['availableDocks'] = station['availableDocks']
			output['availableBikes'] = station['availableBikes']
			output['latitude'] = station['latitude']
			output['longitude'] = station['longitude']
			output['stAddress1'] = station['stAddress1']
			output['lastCommunicationTime'] = station['lastCommunicationTime']
			output['statusValue'] = station['statusValue']
		else:
			output['result'] = 'error'
			output['message'] = 'station not found'
		return json.dumps(output)



	def DELETE(self, sid):
		output = {'result':'success'}
		sid = int(sid)
		self.bdb.delete_station(sid)
		return json.dumps(output)
