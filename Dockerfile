FROM python:3.10

WORKDIR /data-bricks

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

COPY ./config ./config

CMD [ "python","./app/main.py"]

