# Citi Bike Project

## Running the Project
Navigate to the ws_files directory and start up the server with the following command: 
```/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python main.py```
Then, go to http://student04.cse.nd.edu/mwest6/citibikeproject/client/ and use the client, which is now interacting with the server.


## API (api_files folder)

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

## Server (ws_files folder)

The CherryPy server is hosted on student04.cse.nd.edu:52080. 

### User Interaction Functions

(Refer to jsonSpecification.txt for expected inputs/outputs for each request)

/stations/
* ```GET```: view all stations and station information
* ```POST```: send payload with '''{stationName, availableDocks, availableBikes, latitude, longitude, stAddress1, lastCommunicationTime, statusValue}''' to add a new bike station to the database. The new station will be given the next available station id. 
* ```DELETE```: clear database of all station data

/stations/:id
* ```GET```: view station information for specific station id
* ```DELETE```: delete specific station from database

/closest/
* ```POST```: send payload with {latitude, longitude} to get closest station to location

/rent/:id
* ```PUT```: take an available bike out of station x

/park/:id
* ```PUT```: park rented bike at an available dock at station x

/service/:id
* ```GET```: view current service value of station
* ```PUT```: change service value of station to opposite value

### Testing the Server

To test the functionality of the server, navigate to the ws_files directory and start up the server with the following command: 
```/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python main.py```

Once the server is running, run the python script ```python test_ws.py```

## Client (client folder)

The top half of the client contains functions for what a user of Citi Bike might do. This includes finding the closest bike station available, parking or renting a bike, and finding a station name based on its ID. 

The bottom half of the client contains Admin functions, such as adding a new station, deleting a station, and changing the status of a station (whether it is in service or not). 

Demo URL: https://www.youtube.com/watch?v=YWt_EgWPNGQ&feature=youtu.be
