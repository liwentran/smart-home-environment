from flask import Flask, render_template
from flask import Flask
from flask import request
from flask import jsonify, make_response
import json
import sys
import datetime
#sys.path.insert(0, '/home/pi/smart-home-environment/RaspberryPiCode/generate.py') 
#import generate_json.py
#import pi.smart-home-environment.RaspberryPiCode.generate_json
sys.path.append('/home/pi/smart-home-environment/RaspberryPiCode')
import generate_json

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'time': timeString
      }
    return render_template('index.html', **templateData)

@app.route('/postjson', methods=['GET', 'POST'])
def postJsonHandler():
    if request.is_json:
        req = request.get_json()
        response_body = {
            "message": "JSON received!",
            "sender": req.get("name")
        }
        res = make_response(jsonify(response_body), 200)
        return res
        #print (req)
        #return "JSON posted", 200
    else:
        #return "Request was not JSON", 400
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@app.route('/sensordata', methods=['GET', 'POST'])
def sensordata():
    generate_json.generate()
    req = request.get_json()
    
    with open('sensor_data.json') as json_file:
        data = json.load(json_file)
    # response_body = {
    #     "Light Level " : req.get("lightlevel"),
    #     "Fire: " : req.get("fire"),
    #     "Gas: " : req.get("gas"),
    #     "Water Level: " : req.get("waterlevel"),
    #     "Vibration: " : req.get("vibration"),
    #     "Sound Level: " : req.get("soundlevel"),
    #     "Carbon Monoxide: " : req.get("carbonmonoxide")
    # }
    res = make_response(jsonify(data), 200)
    return render_template('data.html', **data)
    
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
