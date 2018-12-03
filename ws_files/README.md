# ws_files

The CherryPy server is hosted on student04.cse.nd.edu:52080. 

### User Interaction

(Refer to jsonSpecification.txt for expected inputs/outputs for each request)

/stations/
* ```GET```: view all stations and station information
* ```POST```: send payload with '''{stationName, availableDocks, availableBikes, latitude, longitue, stAddress1, lastCommunicationTime, statusValue}''' to add a new bike station to the database. The new station will be given the next available station id. 
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


### Testing

To test the functionality of the server, navigate to the ws_files directory and start up the server with the following command: 
```/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python main.py```

Once the server is running, run the python script ```test_ws.py```

### Using the Client

The top half of the client contains functions for what a user of Citi Bike might do. This includes finding the closest bike station available, parking or renting a bike, and finding a station name based on its ID. 

The bottom half of the client contains Admin functions, such as adding a new station, deleting a station, and changing the status of a station (whether it is in service or not). 
