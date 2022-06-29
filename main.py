import shutil
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import requests
import json
import urllib
import os




app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def create_app():

     #print(app)

     return render_template('index.html')


if __name__ == '__main__':

    

    #create_app()

    PORT = os.getenv('PORT', 2000)

    app.run(host="0.0.0.0", debug=True, port = PORT)  #port=PORT
