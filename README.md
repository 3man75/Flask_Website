This is a Flask application takes an online dog API called DOG CEO and takes information from the API. This includes
JSON data from all available species of dogs as well as Dog pictures that show everyones favorite furry friends.

Data Requests are done in the API file and later accessed by the Main.py file. 


## Generating requirements:

from inside the virtualenvironment, 

```
pip freeze > requirements.txt
```

## building the docker container
```
docker build -t <yourname>/dog-website .

docker push <yourname>/dog-website
```

My website can be found on https://flaskdogs.herokuapp.com/ and https://flaskdogs.herokuapp.com/dog.

The first being a webspage that shows the full list of JSON objects that is inside of the Doge CEO app while the second page
utilizes its abiliyt to call up an infinite amount of webpages.

Due to a change in Heroku services for its free tier this project will no longer be updated.

