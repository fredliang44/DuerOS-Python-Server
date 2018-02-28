from app.handler.Main import MainHandler

class DiscoverAppliancesRequestHandler(MainHandler):
    def save(self):
        from models.mysql.activity import Activity
        activity = Activity(
	        sessionId=self.data["session"]["sessionId"],
	        userId=self.data["context"]["System"]["user"]["userId"],
	        applicationID=self.data["context"]["System"]["application"]["applicationId"],
	        apiAccessToken=self.data["context"]["System"]["apiAccessToken"],
	        deviceId=self.data["context"]["System"]["device"]["deviceId"],
	        dialogRequestId=self.data["request"]["dialogRequestId"],
	        requestId=self.data["request"]["requestId"],
	        type=self.data["request"]["type"])
        return activity