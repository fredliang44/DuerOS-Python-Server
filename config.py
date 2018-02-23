from flask import Flask
from app.utils import root
import os
from gunicorn.six import iteritems
import logging
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# pass log to guicorn
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')

# blue print
app.register_blueprint(root, url_prefix='/')

# config
app.config.update(
    DATABASE_TYPE="sqlite",
    SQLITE_DATABASE=os.path.split(os.path.realpath(__file__))[0] + '/database.db',
    SQLALCHEMY_TRACK_MODIFICATIONS= True
)

# config from files
app.config.from_pyfile(os.path.split(os.path.realpath(__file__))[0] + '/settings.cfg', silent=True)


if app.config["DATABASE_TYPE"] == "sqlite":
    prefix = "sqlite:///"
    full_path = app.config['SQLITE_DATABASE']
    app.config['SQLALCHEMY_DATABASE_URI'] = prefix + full_path
    db = SQLAlchemy(app)

elif app.config["DATABASE_TYPE"] == "mysql":
    prefix = "mysql+mysqlconnector://"
    full_path = ''.join([x + app.config[y] for x, y in [['', "MYSQL_USERNAME"], [":", "MYSQL_PASSWORD"], ["@", "MYSQL_HOST"], [':', "MYSQL_PORT"], ['/', "MYSQL_DBNAME"]] if app.config[y] != ""])
    app.config['SQLALCHEMY_DATABASE_URI'] = prefix + full_path
    db = SQLAlchemy(app)

elif app.config["DATABASE_TYPE"] == "mongodb":
    mongo = PyMongo(app)

else:
    raise Exception("Unsupport database type!")

