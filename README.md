# Microservice for Search Index of Phone Numbers

This service checks table for new phone numbers and normalizes it to "9291112233" format. In config you can set timeout between checkouts. Normalized phone numbers inserts into Orders.normalized_phone_number column.

# How to deploy

## To export remote DB use:
```
$ pg_dump -C -h shopscore.devman.org -U score shop > dbexport.pgsql
```
## To create local DB connect to postgres user and via psql use:
```
postgres=# CREATE USER score with password 'Rysherat2';
CREATE ROLE
postgres=# create database shop owner score;
CREATE DATABASE
postgres=# grant postgres to score;
```
## After that to import DB use:
```
$ cat dbexport.pgsql | psql -h localhost -U score shop
```
## To install requirements use:
```
pip install -r requirements.txt
```
## Then you should create alembic directory:
```
(.venv)$ alembic init alembic
```
## Then you should modify alembic.ini and replace sqlalchemy.url to:
```
sqlalchemy.url = postgresql://score:Rysherat2@localhost:5432/shop
```
## Then you can create migration script:
```
(.venv)$ alembic revision -m "create normalized_phone_number column in orders table"
```

# How to run
## In this script you should describe your model and then use migration:
```
$ alembic upgrade head
```
## And run application:
```
$ python3 phone_processing.py
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
