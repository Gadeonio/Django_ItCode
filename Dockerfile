FROM python:3.9

RUN apt update; apt install -y npm

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt; rm /tmp/requirements.txt

COPY . /opt/app
WORKDIR /opt/app

VOLUME /data/

ENV DB_PATH '/data/db.sqlite3'
#ENV SECRET_KEY 'Pain'
EXPOSE 8000

CMD ["sh", "-c", "npm install ; python ./manage.py migrate ; python ./manage.py runserver 0.0.0.0:8000"]


    #["python", "manage.py", "runserver", "0.0.0.0:8000"]

