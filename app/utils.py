from flask import request, Blueprint
# from app.tools.auth import *
from app.tools.record import record
import copy
import json

root = Blueprint('root', __name__)

respond_template = {
    "version": "2.0",
    "context": {
        "intent": {
            "name": "open_lamp",
            "slots": {
                # "{{STRING}}" : {
                #     "name" : "{{STRING}}",
                #     "value" : "{{STRING}}",
                # }
            }
        }
    },
    "session": {
        "attributes": {
            # "{{STRING}}": "{{STRING}}"
        },
    },
    "response": {
        "outputSpeech": {
            "type": "",
            "text": "",
            "ssml": "",
        },
        "reprompt": {
            "outputSpeech": {
                "type": "",
                "text": "",
                "ssml": "root_path",
            }
        },
        "card": {},
        "directives": [],
        "shouldEndSession": False
    }
}


class Lamp:
    def __init__(self, request):
        self.json = copy.deepcopy(respond_template)
        if request["request"]["type"] == "IntentRequest":
            self.json["context"]["intent"]["slots"]["name"] = request["request"]["intents"][0]["slots"]

        self.json["response"]["reprompt"]["outputSpeech"] = {
            "type": "PlainText",
            "text": "hahahahahah",
        }

    def load(self, data):
        self.json["response"]["outputSpeech"] = {
            "type": "PlainText",
            "text": data,
        }

    def respond(self, **kwargs):
        return json.dumps(self.json, indent=2, **kwargs)


@root.route('/', methods=["HEAD", "GET", "POST"])
@record
def appliaction():
    # Respond to health check
    if request.method in ["HEAD", "GET"]:
        return "alive"

    # Handle requests
    elif request.method == "POST":

        data = json.loads(request.data.decode())
        print("========================================request========================================\n")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        handle = Lamp(data)
        handle.load("Recived")
        print(
            "========================================respond========================================\n",
            handle.respond(
                ensure_ascii=False))
        return handle.respond()

    else:
        print(request.method)
        return "error", 404
