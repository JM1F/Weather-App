# Weather-App

This weather app displays weather data for a large amount of cities across the world. 

All data is recieved from https://openweathermap.org/api.

GUI made using [python-tkinter](https://docs.python.org/3/library/tkinter.html)

Two websites are used, one for the REST API and the other is used for city selection and tide times (UK Only).
Either website can be locally hosted or hosted with a third party. (Program currently set up for local host)
Both websites need to be used for the weather app to properly work.

![image](https://user-images.githubusercontent.com/71614127/110513194-de531480-80fd-11eb-92af-e152c9ecf281.png)
* The GUI showing weather data for London.

## How To Use The App For The First Time

#### 1. When you have opened the map website click on the map where you roughly live and a black circle will show the radius of the eligible cities.

![image](https://user-images.githubusercontent.com/71614127/110510489-23c21280-80fb-11eb-9516-bfcbf9738c6b.png)

* The map and tide times (UK) are both hosted on a website. (The source code is currently set to local host)

#### 2. Once the map is clicked the address of the REST API is fetched and the longitude and latitude data is sent to it.
#### 3. Now you need to open the GUI as shown above where you open the settings menu:

<p align="center">
  <img src="https://user-images.githubusercontent.com/71614127/110513736-78b35800-80fe-11eb-8232-3b6d570246e3.png">
</p>

#### 4. Here you can choose your city and the app will save it into a file so you don't have to go through the process again (Unless you want to change cities).

## How It Works

* Coordinates are inputted by the user when the map webpage is clicked.
* This data is then sent to the REST API.
* The REST API then talks to python through [python-flask](https://flask.palletsprojects.com/en/1.1.x/).
* The data is then parsed from the REST API to Python.
***
* (If the data is already saved in the [Location File](https://github.com/JM1F/Weather-App/blob/main/savedLatLngData.txt) then the previous will not be performed if there is a city already saved.)


* The location data is then used as parameters for OpenWeatherMap's API.
```python
url3 = "http://api.openweathermap.org/data/2.5/find?lat={}&lon={}&cnt=10&appid={}".format(lat, long, APIKEY)
```
* Where the GUI on the front-end displays the data recieved from the OpenWeatherMap API. 

## REST API Module
```python
# Rest API sends and recieves data, currently set up for local host.

app = Flask(__name__)
cors = CORS(app)
messages = {}
@app.route('/', methods=['GET', "PUT", "POST"])
def flaskREST():
   
    # POST request
    if request.method == 'POST':
        try:
            print('Incoming...')
            Long = request.get_json("long")
            messages["coords"] = Long
            print(messages)
            return jsonify(messages)
        except:
            print("An Error Occured...")

    # GET request
    if request.method == "GET":
        try:
            return jsonify(messages)  
        except:
            print("An Error Occured...")

    # PUT request
    if request.method == "PUT":
        try:
            Long = request.get_json("long")
            messages["coords"] = Long
            print(messages)
            return jsonify(messages)
        except:
            print("An Error Occured...")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
````

* Currently set to local host. (127.0.0.1:5000)
