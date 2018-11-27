import unittest
import requests
import json

class TestWebService(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52080' 
	STATIONS_URL = SITE_URL + '/stations/'
	CLOSEST_URL = SITE_URL + '/closest/'
	RENT_URL = SITE_URL + '/rent/'
	PARK_URL = SITE_URL + '/park/'
	SERVICE_URL = SITE_URL + '/service/'
	RESET_URL = SITE_URL + '/reset/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	#reset data
	def reset_data(self):
		m={}
		r = requests.put(self.RESET_URL, data=json.dumps(m))

	#test stations_get_all



	#test stations_post


	
	#test stations_delete_all

	
	#test stations_get
	def test_stations_get(self):
		self.reset_data()
		station_id = 281
		r = requests.get(self.STATIONS_URL + str(station_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['stationName'], 'Grand Army Plaza & Central Park S')
		self.assertEqual(resp['availableDocks'], 13)
		self.assertEqual(resp['availableBikes'], 36)
		self.assertEqual(resp['latitude'], 40.7643971)
		self.assertEqual(resp['longitude'], -73.97371465)
		self.assertEqual(resp['stAddress1'], 'Grand Army Plaza & Central Park S')
		self.assertEqual(resp['lastCommunicationTime'], '2018-11-05 01:12:05 PM')
		self.assertEqual(resp['statusValue'], 'In Service')

	#test stations_delete
	def test_stations_delete(self):
		self.reset_data()
		station_id = 281

		m = {}
		r = requests.delete(self.STATIONS_URL + str(station_id), data=json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.STATIONS_URL + str(station_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')

	#test closest_post

	def test_closest_post(self):
		self.reset_data()
		m = {}
		m['latitude'] = 40.7643971 
		m['longitude'] = -73.97371465
		r = requests.post(self.CLOSEST_URL, json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEquals(resp['station_id'], 281) 

	#test rent_put



	#test park_put



	#test service_get


	#test service_put

if __name__ == "__main__":
	unittest.main()
