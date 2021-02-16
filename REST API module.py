from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
# Rest API sends and recieves data, currently set up for local host.

app = Flask(__name__)
cors = CORS(app)
messages = {}
@app.route('/', methods=['GET', "PUT", "POST"])
def hello():
   
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
   
