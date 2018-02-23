import json
from functools import wraps
from app.utils import request


def record(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if request.method == "POST":
            data = json.loads(request.data.decode())
            from dueros import app
            if app.config["DATABASE_TYPE"] == "mongodb":
                from dueros import mongo
                mongo.db.activity.insert_one(data)

            elif app.config["DATABASE_TYPE"] in ["sqlite", "mysql"]:
                from models.mysql.activity import Activity
                from config import db
                if data["request"]["type"] == "SessionEndedRequest":
                    activity = Activity(sessionId=data["session"]["sessionId"],
                                        applicationID=data["context"]["System"]["application"]["applicationId"],
                                        userId=data["context"]["System"]["user"]["userId"],
                                        apiAccessToken=data["context"]["System"]["apiAccessToken"],
                                        deviceId=data["context"]["System"]["device"]["deviceId"],
                                        dialogRequestId=data["request"]["dialogRequestId"],
                                        requestId=data["request"]["requestId"],
                                        type=data["request"]["type"])

                elif data["request"]["type"] == "IntentRequest":
                    activity = Activity(sessionId=data["session"]["sessionId"],
                                        applicationID=data["context"]["System"]["application"]["applicationId"],
                                        apiAccessToken=data["context"]["System"]["apiAccessToken"],
                                        userId=data["context"]["System"]["user"]["userId"],
                                        deviceId=data["context"]["System"]["device"]["deviceId"],
                                        query=data["request"]["query"]["original"],
                                        dialogRequestId=data["request"]["dialogRequestId"],
                                        requestId=data["request"]["requestId"],
                                        dialogState=data["request"]["dialogState"],
                                        type=data["request"]["type"])

                elif data["request"]["type"] == "LaunchRequest":
                    activity = Activity(sessionId=data["session"]["sessionId"],
                                        applicationID=data["context"]["System"]["application"]["applicationId"],
                                        apiAccessToken=data["context"]["System"]["apiAccessToken"],
                                        userId=data["context"]["System"]["user"]["userId"],
                                        deviceId=data["context"]["System"]["device"]["deviceId"],
                                        dialogRequestId=data["request"]["dialogRequestId"],
                                        requestId=data["request"]["requestId"],
                                        type=data["request"]["type"])
                else:
                    raise Exception("Invaid Database")

                db.session.add(activity)
                db.session.commit()
                print("\n\nADDED\n\n")
            else:
                pass
            return fn(*args, **kwargs)
        else:
            return 'alive'
    return wrapper
