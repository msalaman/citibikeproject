import cherrypy
import re, json
from _citibike_database import _citibike_database

class ResetController(object):
	def __init__(self, bdb):
		self.bdb=bdb


	def PUT(self):
		output = {'result':'success'}
		self.bdb.reset_data()
		return json.dumps(output)
