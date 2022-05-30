import shutil
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import requests
import json
import urllib
import api



app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def create_app():

    print(app)

    return returned_dict

@app.route('/dog')
def doggies():

    doggy= api.get_dog_images() #NameError: api is not defined

    return render_template("dog.html", dog=doggy)

if __name__ == '__main__':

    #Calls JSON_Data and sends it to the initial flask page
    returned_dict = api.get_dogs()

    #Creates first website
    create_app()

    app.run(host="0.0.0.0", debug=True, port=2000)
