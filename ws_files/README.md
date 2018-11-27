# ws_files

The CherryPy server is hosted on student04.cse.nd.edu:52080. 

### User Interaction

/stations/
* '''GET''': view all stations and station information
* '''POST''': send payload with '''{stationName, availableDocks, availableBikes, latitude, longitue, stAddress1, lastCommunicationTime, statusValue}''' to add a new bike station to the database. The new station will be given the next available station id. 
* '''DELETE''': clear database of all station data

/stations/:id
* '''GET''': view station information for specific station id
* '''DELETE''': delete specific station from database

/closest/
* '''POST''': send payload with {latitude, longitude} to get closest station to location

/rent/:id
* '''PUT''': take an available bike out of station x

/park/:id
* '''PUT''': park rented bike at an available dock at station x

/service/:id
* '''GET''': view current service value of station
* '''PUT''': change service value of station to opposite value

