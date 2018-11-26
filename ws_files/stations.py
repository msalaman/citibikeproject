import json
import requests
import cherrypy

from _citibike_database import _movie_database

class StationsController(object): 
	def __init(self, bdb):
		self.bdb=bdb



	

	GET(self, sid):
		output = {'result':'success'}
		sid = int(sid)
		station = self.bdb.get_station(sid)
		if station != None:
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


	DELETE(self, sid):
		output = {'result':'success'}
		sid = int(sid)
		self.bdb.delete_station(sid)
		return json.dumps(output)
