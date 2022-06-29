This is a small Flask application to create a website for the hit Mobile game Fate Grand Order.


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