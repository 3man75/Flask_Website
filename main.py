import shutil
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import requests
import json
import urllib
import api
import os



app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def create_app():

    print(app)

    return returned_dict

@app.route('/dog')
def doggies():

    #calls the function in the api file
    doggy= api.get_dog_images()

    return render_template("dog.html", dog=doggy)

if __name__ == '__main__':

    #Calls JSON_Data and sends it to the initial flask page from api file
    returned_dict = api.get_dogs()

    #Creates first website
    create_app()

    PORT = os.getenv('PORT', 2000)

    app.run(host="0.0.0.0", debug=True, port=PORT)
