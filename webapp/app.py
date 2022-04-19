from flask import Flask, render_template
from flask import Flask
from flask import request
from flask import jsonify, make_response
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'time': timeString
      }
    return render_template('index.html', **templateData)

@app.route('/postjson', methods=['POST'])
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
    
#@app.route('/secondPage')
#def pageTwo():
    #return 'this is page 2'

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
