# api_files

### Data source

Data is JSON format from NYCOpenData CitiBike statistics. The data source is updated frequently with stats from docking stations throughout the city. It provides info on number of bikes available, number of bike parking docks available, the location of station (latitude and longitude), and station name, address and ID.

https://feeds.citibikenyc.com/stations/stations.json

### User Interaction 

A user will receive the number of available docks or number of a available bikes, the address of this docking station,  and its distance from them based on their latitude and longitude, and whether it is in service or not. 

#### _citibike_database.py

* ```load_stations```: loads json from data file into a formatted dictionary
* ```get_station(sid)```: returns data for specified station
* ```park_bike(sid)```: increases available bikes for specific station by 1, decreases available docks of specific station by 1
* ```rent_bike(sid```): decreases available bikes for specific station by 1, increases available docks of specific station by 1
* ```reset_data```: resets dictionary to original values from data file
* ```get_service(sid)```: returns if bike station is in service or not
* ```update_service(sid)```: changes service value for bike station
* ```get_closest_station(latitude, longitude)```: returns information for closest station to users inputted latitude and longitude
* ```delete_station(sid)```: deletes specific station from dictionary
* ```delete_all_stations```: clears dictionary of all stations


### Test

To test the functionality of _citibike_database.py, run ```python3 test_api.py``` in the api_files directory. This test file tests the functions created in the _citibike_database class. 
