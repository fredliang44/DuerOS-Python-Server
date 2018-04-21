import logging
import os

from app.request import root
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from gunicorn.six import iteritems

app = Flask(__name__)

"""
blue print
"""
app.register_blueprint(root, url_prefix='/')

"""
default config
"""
app.config.update(
    DATABASE_TYPE="sqlite",
    SQLITE_DATABASE=os.path.split(
        os.path.realpath(__file__))[0] +
    '/database.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=True)

"""
config from files
"""
app.config.from_pyfile(
    os.path.split(
        os.path.realpath(__file__))[0] +
    '/settings.cfg',
    silent=True)
