
var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic2hhcnBpc2hhIiwiYSI6ImNrOXl6MGNqaDAzZDgzZW1kenh5YTNnYTEifQ.B5P5MEel2ZJVtBYXedV2mA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
}).addTo(mymap);

var marker = L.marker();

var circle = L.circle();
// Sending data to the rest API, currently set up for local host
function transmitDatafetch(lat, lng) {
    try {

        fetch('http://localhost:5000/', {
            // GET, POST, PUT, DELETE METHODS
            method: 'PUT',
            // Send body of data to REST api
            body: JSON.stringify({
                "lat": lat,
                "long": lng
            })
        }).then(function (response) {
            return response.text();
        }).then(function (text) {
        });
    } catch (e) {
        console.log("No Connection Established With Rest API");
    }
    
}   
// Function for clicking on the map 
function onMapClick(e) {
    console.log(e.latlng.lat);
    marker.setLatLng([e.latlng.lat, e.latlng.lng]).addTo(mymap)
    console.log(e.latlng.lng);
    circle.options.color = "black";
    console.log(circle.options)
    circle.options.opacity = 1;
    circle.setLatLng([e.latlng.lat, e.latlng.lng]).setRadius(22000).addTo(mymap)
    transmitDatafetch(e.latlng.lat, e.latlng.lng);
  
}

mymap.on("click", onMapClick);
