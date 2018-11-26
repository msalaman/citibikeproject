import cherrypy
import re, json 
from __database import _movie_database
class CloseController(object):
	def __init__(self, bdb):
		self.bdb=bdb
		
	
	def POST(self):
		output = {'result':'success'}
		data = json.loads(cherrypy.request.body.read())
		lat = data[0]
		lon = data[1]
		sid = self.bdb.get_closest(lat, lon)
		output['station_id'] = sid
		return json.dumps(output)
