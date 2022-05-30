This is a small Flask application takes an online dog API called DOG CEO and takes information from the API. This includes
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


