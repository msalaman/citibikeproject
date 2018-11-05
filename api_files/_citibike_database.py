class _citibike_database: 

	def __init__(self):
		self.stations = list()

	def load_stations(self, station_file):
		f = open(station_file)
		# parse json here
		f.close()


if __name__ == "__main__":
	db = _citibike_database()

	db.load_stations('bikeStations.dat')
	



