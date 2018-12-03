function addStation(){
	var req = new XMLHttpRequest();
	req.open("POST", "http://student04.cse.nd.edu:52080/stations/", true);
    var data = {};

    data.stationName = document.getElementById('addStationName').value;
    data.availableDocks = parseInt(document.getElementById('addAvailDocks').value);
    data.availableBikes = parseInt(document.getElementById('addAvailBikes').value);
    data.latitude = parseInt(document.getElementById('addLatitude').value);
    data.longitude = parseInt(document.getElementById('addLongitude').value);
    data.stAddress1 = document.getElementById('addAddress').value;
    data.lastCommunicationTime = document.getElementById('addLastCommTime').value;
    data.statusValue = document.getElementById('addStatus').value;
    var json = JSON.stringify(data);

	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			alert('Successfully added station ' + response.id);
            document.getElementById('addStationName').value = ''; 
	        document.getElementById('addAvailDocks').value = ''; 
            document.getElementById('addAvailBikes').value = ''; 
            document.getElementById('addLatitude').value = ''; 
	        document.getElementById('addLongitude').value = ''; 
            document.getElementById('addAddress').value = ''; 
            document.getElementById('addLastCommTime').value = ''; 
            document.getElementById('addStatus').value = ''; 
        }
	}

	req.send(json);

}

function deleteStation(){
	sid = document.getElementById('delStationID').value;
	var req = new XMLHttpRequest();
	req.open("DELETE", "http://student04.cse.nd.edu:52080/stations/" + sid, true);

	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			alert('Successfully deleted station ' + sid);
            document.getElementById('delStationId').value = '';
		}
	}

	req.send(null);
}

function changeStatus(){
    sid = document.getElementById('changeStationStatus').value;
	var req = new XMLHttpRequest();
	req.open("PUT", "http://student04.cse.nd.edu:52080/service/" + sid, true);
    var data = {};
    var json = JSON.stringify(data);

	req.onload = function(e){
		response = JSON.parse(req.responseText);
		if (response.result == 'success'){
			alert('Successfully changed status on station ' + sid);
            document.getElementById('changeStationStatus').value = ''; 
		}
	}

	req.send(json);

}
