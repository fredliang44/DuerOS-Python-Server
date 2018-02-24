import json

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

class IntentRequestHandler:
    def __init__(self, data):
        self.__got_all_data = []
        self.__got_data = None

        if isinstance(data, dict):
            self.data = data
        elif isinstance(data, (str, bytes)):
            self.data = json.loads(data)
        else:
            raise Exception("Unsupport IntentRequestHandler data type!")

    def get(self, key):
        self.traversal_dict(key, self.data, all=True)
        return self.__got_data

    def get_all(self, key):
        self.traversal_dict(key, self.data, all=False)
        return self.__got_all_data

    """traversal to search key"""

    def traversal_dict(self, key, dictionary, all):
        if isinstance(dictionary, dict):
            for x in range(len(dictionary)):
                temp_key = list(dictionary.keys())[x]
                temp_value = dictionary[temp_key]
                if temp_key == key:
                    if all:
                        self.__got_all_data.extend(temp_value)
                    else:
                        self.__got_data = temp_value
                    return

                self.traversal_dict(key, temp_value, all=all)
        else:
            return None
