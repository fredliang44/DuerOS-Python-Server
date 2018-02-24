from app.handler.Main import MainHandler
"""
example = {
    "session": {
        "sessionId": "4477caec-2db7-495e-aec3-a0352df7dfdd",
        "new": True
    },
    "context": {
        "System": {
            "user": {
                "userInfo": {
                    "account": {}
                },
                "userId": "67037059"
            },
            "apiAccessToken": "Qt6KU05S/GlHDwTwaLnJBGiO7Ior4oWY97K2VVspnhAOZ+A6daVxe74yQ3RT4E4gk/2EsmVumNX/4hJFR4RgQsY8bjMC6szTtwj8Xh7d48EiS+L37J9MGuxXwGCpxbz0xPIG32Q4JRYZUTbhBrKuYtNmIj8OA1XZyXJ16Stow4c5gfWapy3ffVAmMLvmCjTKnittLt52WUm/8XcyxbNjq3N1lWbbVvrDuN7DVc453siBOo8tQjc0Lia40smX8JAYLqh5mQydrFMQb1iQoUrr+3K6idY8wYy92kWZM6zM/BIAGO+Jt8sRThOyCMK1OWRU",
            "application": {
                "applicationId": "2fc548c7-018a-92a5-a497-a8b824495949"
            },
            "apiEndPoint": "https://xiaodu.baidu.com",
            "device": {
                "supportedInterfaces": {
                    "VoiceInput": {},
                    "VoiceOutput": {},
                    "AudioPlayer": {}
                },
                "deviceId": "85713227b58458938501b00be7bbeb5d"
            }
        }
    },
    "request": {
        "timestamp": "1519463420",
        "intents": [{
                    "slots": {
                        "action": {
                            "value": "打开",
                            "name": "action",
                            "values": [
                                "打开"
                            ],
                            "confirmationStatus": "NONE"
                        },
                        "object": {
                            "value": "台灯",
                            "name": "object",
                            "values": [
                                "台灯"
                            ],
                            "confirmationStatus": "NONE"
                        }
                    },
                    "name": "open_lamp",
                    "confirmationStatus": "NONE"
                    }],
        "dialogRequestId": "760a8697-3227-43cd-afbe-f20c920aeacc",
        "type": "IntentRequest",
                "dialogState": "STARTED",
                "query": {
            "type": "TEXT",
            "original": "开台灯"
        },
        "requestId": "c7389306451d4966a2cac1073d202f69_0"
    },
    "version": "v2.0"
}
"""

class IntentRequestHandler(MainHandler):
    def save(self):
        from models.mysql.activity import Activity
        activity = Activity(
            sessionId=self.data["session"]["sessionId"],
            userId=self.data["context"]["System"]["user"]["userId"],
            applicationID=self.data["context"]["System"]["application"]["applicationId"],
            apiAccessToken=self.data["context"]["System"]["apiAccessToken"],
            query=self.data["request"]["query"]["original"],
            deviceId=self.data["context"]["System"]["device"]["deviceId"],
            dialogRequestId=self.data["request"]["dialogRequestId"],
            requestId=self.data["request"]["requestId"],
            dialogState=self.data["request"]["dialogState"],
            type=self.data["request"]["type"])
        return activity