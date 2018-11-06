# test file
from _citibike_database import _citibike_database
import unittest

class TestCitibikeDatabase(unittest.TestCase):
	
      db = _citibike_database()

      def reset_data(self):
        self.db.reset_data()

      def test_get_station(self):
        self.reset_data()
        station = self.db.get_station('281')
        self.assertEquals(station['stationName'], 'Grand Army Plaza & Central Park S')
        station = self.db.get_station('999999')
        self.assertEquals(station, 'error')
      
      def test_park_bike(self):
        self.reset_data()
        self.db.park_bike('281')
        station = self.db.get_station('281')
        self.assertEquals(station['availableBikes'], 37)
        self.assertEquals(station['availableDocks'], 13)
        self.assertEquals(db.park_bike('999999'), 'error')
        
      def test_rent_bike(self):
        self.reset_data()
        self.db.park_bike('281')
        station = self.db.get_station('281')
        self.assertEquals(station['availableBikes'], 35)
        self.assertEquals(station['availableDocks'], 15)
        self.assertEquals(db.park_bike('999999'), 'error')
      
      
      
      def test_get_service(self):
        self.reset_data()
        service = self.db.get_service('281')
        self.assertEquals(service, "In Service")
      
      def test_update_service(self):
      	self.reset_data()
        self.db.update_service('281')
        station = self.db.get_station('281')
        self.assertEquals(station['statusValue'], "Not In Service")
      
      def test_get_closest_station(self):
        self.reset_data()
        closestStation = self.db.get_closest_station(40.76, -73.97)
        closest = closestStation['stationName']
        self.assertEquals('Grand Army Plaza & Central Park S', closest)
      
      def test_delete_station(self):
        self.reset_data()
        self.db.delete_station('281') # test delete station 281
        station = self.db.get_station('281')
      	self.assertEquals(station, None)
        


if __name__ == "__main__":
	unittest.main()
