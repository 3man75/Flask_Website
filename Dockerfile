FROM python:3.8-alpine

COPY . /usr/src/app
RUN ls -la /usr/src/app

WORKDIR /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 2000
CMD ["python", "main.py"]