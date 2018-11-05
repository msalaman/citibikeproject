import requests
import json

class _citibike_database: 

	def __init__(self):
		self.stations = dict()

	def load_stations(self, station_file):
		f = open(station_file)
		data = json.load(f)
		f.close()
		for station in data['stationBeanList']:
			key = station['id']
			temp = {}
			temp['stationName'] = station['stationName']
			temp['availableDocks'] = station['availableDocks']
			temp['latitude'] = station['latitude']
			temp['longitude'] = station['longitude']
			temp['availableBikes'] = station['availableBikes']
			temp['stAddress1'] = station['stAddress1']
			temp['lastCommunicationTime'] = station['lastCommunicationTime']
			temp['statusValue'] = station['statusValue']
			self.stations[key] = temp			
		print(self.stations)
        
	def load_station(self, station_file, sid):
		return 0		


if __name__ == "__main__":
	db = _citibike_database()

	db.load_stations('bikeStations.dat')
	



