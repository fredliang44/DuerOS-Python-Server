import json
from functools import wraps
from app.utils import request
from app.handler import IntentRequest, SessionEndedRequest, LaunchRequest

def transform_to_sql(data):
	if data["request"]["type"] == "SessionEndedRequest":
		activity = SessionEndedRequest.SessionEndedRequestHandler(data).save()
	elif data["request"]["type"] == "IntentRequest":
		activity = IntentRequest.IntentRequestHandler(data).save()
	elif data["request"]["type"] == "LaunchRequest":
		activity = LaunchRequest.LaunchRequestRequestHandler(data).save()
	else:
		raise Exception("Invaid request method")
	return activity


def save(data):
	from dueros import app
	if app.config["DATABASE_TYPE"] == "mongodb":
		from dueros import mongo
		mongo.db.activity.insert_one(data)

	elif app.config["DATABASE_TYPE"] in ["sqlite", "mysql"]:
		from config import db

		activity = transform_to_sql(data)

		db.session.add(activity)
		db.session.commit()

	else:
		raise Exception("Invaid Database")


def record(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if request.method == "POST":
			data = json.loads(request.data.decode())
			save(data)
			return fn(*args, **kwargs)
		else:
			return 'alive'
	return wrapper
