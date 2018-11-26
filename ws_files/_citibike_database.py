import requests
import json
import math

class _citibike_database:

	def __init__(self):
		self.stations = dict()

	def load_stations(self, station_file):
		''' load info from file into local datasource self.stations
		{
			sid: {
				"stationName": str,
				"availableDocks": int,
				"availableBikes": int,
				"latitude": float,
				"longitude": float,
				"stAddress1": str,
				"lastCommunicationTime": str,
				"statusValue": str
			},
			
			sid: { }
		}
		'''

		f = open(station_file)
		data = json.load(f)
		f.close()
		for station in data['stationBeanList']:
			key = station['id']
			temp = {}
			temp['stationName'] = station['stationName']
			temp['availableDocks'] = int(station['availableDocks'])
			temp['availableBikes'] = int(station['availableBikes'])
			temp['latitude'] = float(station['latitude'])
			temp['longitude'] = float(station['longitude'])
			temp['stAddress1'] = station['stAddress1']
			temp['lastCommunicationTime'] = station['lastCommunicationTime']
			temp['statusValue'] = station['statusValue']
			self.stations[key] = temp
		#print(self.stations)

	def get_station(self, sid):
	# get information for a station ID
		if sid in self.stations.keys():
			return self.stations[sid]
		else:
			return 'error'

	def park_bike(self, sid):
	# user is going to park a bike, reduce available bikes at station sid by 1
		if sid in self.stations:
			self.stations[sid]['availableBikes'] = self.stations[sid]['availableBikes'] + 1
			self.stations[sid]['availableDocks'] = self.stations[sid]['availableDocks'] - 1
		else:
			return "error"

	def rent_bike(self, sid):
	# user is going to rent a bike, increase available bikes at station sid by 1
		if sid in self.stations:
			self.stations[sid]['availableBikes'] = self.stations[sid]['availableBikes'] - 1
			self.stations[sid]['availableDocks'] = self.stations[sid]['availableDocks'] + 1
		else:
			return "error"

	def reset_data(self):
	# reset data to original values from data file
		self.load_stations('bikeStations.dat')

	def get_service(self, sid):
	# returns the status of bike station
		if sid in self.stations:
			return self.stations[sid]['statusValue']
		else:
			return "error"

	def update_service(self, sid):
	# change status value of bike station
		if sid in self.stations:
			if self.stations[sid]['statusValue'] == "In Service":
				self.stations[sid]['statusValue'] = "Not In Service"
			elif self.stations[sid]['statusValue'] == "Not In Service":
				self.stations[sid]['statusValue'] = "In Service"

	def get_closest_station(self, my_lat, my_long):
		# returns station that is closest to users latitude and longitude
		my_lat = float(my_lat)
		my_long = float(my_long)

		minDistance = 1000000000
		minID = -1

		for station in self.stations:
			lat = self.stations[station]['latitude']
			long_ = self.stations[station]['longitude']
			distance = math.sqrt((my_long - long_)**2 + (my_lat - lat)**2)
			if distance <= minDistance:
					minDistance = distance
					minID = station

		if minID < 0:
			return "error"

		# print("DISTANCE: " + minDistance)
		# print("DISTANCE: " + minDistance)
		return self.stations[minID]


	def delete_station(self, sid):
		if sid in self.stations:
			del self.stations[sid]
		else:
			return None

	def delete_all_stations(self):
		self.stations.clear()


if __name__ == "__main__":
	db = _citibike_database()

	db.load_stations('bikeStations.dat')

	db.get_station('281')
