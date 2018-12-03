function findStation(){ 
	var lat = document.getElementById('closeLat').value; 
	var long = document.getElementById('closeLong').value;
	var req = new XMLHttpRequest();
	req.open("POST", "http://student04.cse.nd.edu:52080/closest/", true);
    	var data = {};

    	data.latitude = parseInt(lat);
    	data.longitude = parseInt(long);
    	var json = JSON.stringify(data);

	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			var newP = document.createElement("p"); // create this.item
			var node = document.createTextNode("The closest station to the coordinates {" + lat + ", " + long + "} is station " + response.station_id)
			newP.appendChild(node);
			newP.classList.add("addedP");
			document.getElementById('closeField').appendChild(newP); 
            		document.getElementById('closeLat').value = ''; 
	        	document.getElementById('closeLong').value = ''; 
        	}
	}

	req.send(json);
} 

function parkBike(){ 
	var x = document.getElementById('parkId').value;
	
	var req = new XMLHttpRequest();
	req.open("PUT", "http://student04.cse.nd.edu:52080/park/" + x, true);

	var data = {};
    	var json = JSON.stringify(data);
	console.log("here");
	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			alert('Successfully parked bike at station ' + x);
            		document.getElementById('changeStationStatus').value = ''; 
            		document.getElementById('parkId').value = ''; 
        	}
	}

	req.send(json);
	
} 


function pickUpBike(){ 
	var x = document.getElementById('parkId').value;
	
	var req = new XMLHttpRequest();
	req.open("PUT", "http://student04.cse.nd.edu:52080/rent/" + x, true);

	var data = {};
    	var json = JSON.stringify(data);
	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			alert('Successfully picked up bike at station ' + x);
            		document.getElementById('changeStationStatus').value = ''; 
            		document.getElementById('parkId').value = ''; 
        	}
	}

	req.send(json);
} 

function stationName(){ 
	var name = document.getElementById('nameId').value;
	var req = new XMLHttpRequest();
	req.open("GET", "http://student04.cse.nd.edu:52080/stations/" + name, true);

    	var data = {};
    	var json = JSON.stringify(data);

	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			var newP = document.createElement("p"); // create this.item
			var node = document.createTextNode("The name of station " + name + " is " + response.stationName);
			newP.classList.add("addedP");
			newP.appendChild(node);
			document.getElementById('nameField').appendChild(newP); 
            		document.getElementById('nameId').value = '';
        	}
	}

	req.send(json);
} 


function stationStatus(){ 
	var name = document.getElementById('nameId').value;
	var req = new XMLHttpRequest();
	req.open("GET", "http://student04.cse.nd.edu:52080/service/" + name, true);

    	var data = {};
    	var json = JSON.stringify(data);

	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			console.log(response); 
			var newP = document.createElement("p"); // create this.item
			var node = document.createTextNode("Station " + name + " is " + response.value);
			newP.classList.add("addedP");
			newP.appendChild(node);
			document.getElementById('nameField').appendChild(newP); 
            		document.getElementById('nameId').value = '';
        	}
	}

	req.send(json);
} 

