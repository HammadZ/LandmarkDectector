from google.cloud import vision
from google.cloud.vision import types
from flask import Flask, request
import json
import base64
app = Flask(__name__)


with open("index.html") as indexfile:
	index_text = indexfile.read()

app = Flask(__name__)
@app.route("/")
def hello():
    return index_text

import io
import os


# Instantiates a client
client = vision.ImageAnnotatorClient()


@app.route('/request', methods=['POST'])
def req():
	# open used for testing purposes
    open("out", 'wb').write(request.data) 
    # open used for testing purposes
    image = types.Image(content=request.data)
    response = client.landmark_detection(image=image)
    print(response.landmark_annotations)
    return json.dumps([{
        "latitude": j.lat_lng.latitude,
        "longitude": j.lat_lng.longitude,
        }  for i in response.landmark_annotations for j in i.locations])



# Create another file with AJAX request
# Has me return the JSON file with long and Lat
# Send the JSON long/lat to the MAPS API and display location of landmark
