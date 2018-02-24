import json
from functools import wraps
from app.utils import request

def transform_sql(data):
	from models.mysql.activity import Activity
	if data["request"]["type"] == "SessionEndedRequest":
		activity = Activity(sessionId=data["session"]["sessionId"], userId=data["context"]["System"]["user"]["userId"],
		                    applicationID=data["context"]["System"]["application"]["applicationId"],
		                    apiAccessToken=data["context"]["System"]["apiAccessToken"],
		                    deviceId=data["context"]["System"]["device"]["deviceId"],
		                    requestId=data["request"]["requestId"],type=data["request"]["type"])
	elif data["request"]["type"] == "IntentRequest":
		activity = Activity(sessionId=data["session"]["sessionId"], userId=data["context"]["System"]["user"]["userId"],
		                    applicationID=data["context"]["System"]["application"]["applicationId"],
		                    apiAccessToken=data["context"]["System"]["apiAccessToken"],
		                    query=data["request"]["query"]["original"],
		                    deviceId=data["context"]["System"]["device"]["deviceId"],
		                    dialogRequestId=data["request"]["dialogRequestId"],
		                    requestId=data["request"]["requestId"],
		                    dialogState=data["request"]["dialogState"],type=data["request"]["type"])
	elif data["request"]["type"] == "LaunchRequest":
		activity = Activity(sessionId=data["session"]["sessionId"], userId=data["context"]["System"]["user"]["userId"],
		                    applicationID=data["context"]["System"]["application"]["applicationId"],
		                    apiAccessToken=data["context"]["System"]["apiAccessToken"],
		                    deviceId=data["context"]["System"]["device"]["deviceId"],
		                    dialogRequestId=data["request"]["dialogRequestId"],
		                    requestId=data["request"]["requestId"],type=data["request"]["type"])
	else: raise Exception("Invaid request method")
	return activity

def save(data):
	from dueros import app
	if app.config["DATABASE_TYPE"] == "mongodb":
		from dueros import mongo
		mongo.db.activity.insert_one(data)

	elif app.config["DATABASE_TYPE"] in ["sqlite", "mysql"]:
		from config import db

		activity =  transform_sql(data)

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
