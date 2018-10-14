# Microservice for Search Index of Phone Numbers

To export remote DB use:
```
$ pg_dump -C -h shopscore.devman.org -U score shop > dbexport.pgsql
```
To create local DB connect to postgres user and via psql use:
```
postgres=# CREATE USER score with password 'Rysherat2';
CREATE ROLE
postgres=# create database shop owner score;
CREATE DATABASE
postgres=# grant postgres to score;
```
After that to import DB use:
```
$ cat dbexport.pgsql | psql -h localhost -U score shop
```
To install requirements use:
```
pip install -r requirements.txt
```
Then you should create alembic directory:
```
(.venv)$ alembic init alembic
```
Then you should modify alembic.ini and replace sqlalchemy.url to:
```
sqlalchemy.url = postgresql://score:Rysherat2@localhost:5432/shop
```
Then you can create migration script:
```
(.venv)$ alembic revision -m "create normalized_phone_number column in orders table"
```
In this script you shoul describe your model and then use migration:
```
$ alembic upgrade head
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
