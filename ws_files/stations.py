import json
import requests
import cherrypy

from _citibike_database import _citibike_database


class StationsController(object):
	def __init__(self, bdb):
		self.bdb=bdb


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

	# /stations/
	def GET_STATIONS(self):
		l = []
		for i in self.bdb.stations:
			station = self.bdb.get_station(i)
			temp = {}

			temp['stationName'] = station['stationName']
			temp['availableDocks'] = station['availableDocks']
			temp['availableBikes'] = station['availableBikes']
			temp['latitude'] = station['latitude']
			temp['longitude'] = station['longitude']
			temp['stAddress1'] = station['stAddress1']
			temp['lastCommunicationTime'] = station['lastCommunicationTime']
			temp['statusValue'] = station['statusValue']
			l.append(temp)

		output = {'result':'success', 'stations':l}
		return json.dumps(output)

	def POST_STATIONS(self):
		output = {'result':'success'}
		data = json.loads(cherrypy.request.body.read())
		temp = {}

		try:
			temp['stationName'] = data['stationName']
			temp['availableDocks']  = data['availableDocks']
			temp['availableBikes']  = data['availableBikes']
			temp['latitude'] = data['latitude']
			temp['longitude']  = data['longitude']
			temp['stAddress1']  = data['stAddress1']
			temp['lastCommunicationTime'] = data['lastCommunicationTime']
			temp['statusValue'] = data['statusValue']

			sid = list(self.bdb.stations.keys())[-1] + 1
			sid = int(sid)
			self.bdb.stations[sid] = temp
			output['id'] = sid

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE_ALL(self):
		output = {'result':'success'}
		self.bdb.delete_all_stations()
		return json.dumps(output)
