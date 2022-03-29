from flask import Flask, render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/secondPage')
#def pageTwo():
    #return 'this is page 2'

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
