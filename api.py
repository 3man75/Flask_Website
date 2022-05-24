import shutil
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import requests
import json
from PIL import Image
import urllib


def get_dogs():
    #this function gets data on all dogs from the API through JSON but not there images.

    url = "https://dog.ceo/api/breeds/list/all"

    dogRequest1 = requests.get(url) #uses request module to access the url provided above
    
    dogs = dogRequest1.json()

    return dogs.get("message")

def get_dog_images():
    imageUrl = "https://dog.ceo/api/breed/hound/images/random"

    #dog_request = requests.get(imageUrl)  #Here I get it from the web

    dog_image = dog_request.json()["message"]

    return dog_image
