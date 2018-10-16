import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://score:Rysherat2@localhost:5432/shop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CHECK_NEW_ORDERS_TIMEOUT = 10
