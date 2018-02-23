from flask import request, Blueprint
from app.tools.auth import *
import copy
import json
root = Blueprint('root', __name__)

res_tem = {
    "version" : "2.0",
    "context" : {
        "intent" : {
            "name" : "open_lamp",
            "slots" : {
                # "{{STRING}}" : {
                #     "name" : "{{STRING}}",
                #     "value" : "{{STRING}}",
                # }
            }
        }
    },
    "session" : {
        "attributes" : {
            # "{{STRING}}": "{{STRING}}"
        },
    },
    "response" : {
        "outputSpeech" : {
            "type" : "",
            "text" : "",
            "ssml" : "",
        },
        "reprompt" : {
            "outputSpeech" : {
                "type" : "",
                "text" : "",
                "ssml" : "root_path",
            }
        },
        "card" : {},
        "directives" : [],
        "shouldEndSession" : False
    }
}

class Lamp:
    def __init__(self,request):
        self.json = copy.deepcopy(res_tem)
        if  request["request"]["type"] == "IntentRequest":
            self.json["context"]["intent"]["slots"]["name"] =  request["request"]["intents"][0]["slots"]

        self.json["response"]["reprompt"]["outputSpeech"] = {
            "type": "PlainText",
            "text": "hahahahahah",
        }

    def load(self,data):
        self.json["response"]["outputSpeech"] = {
            "type": "PlainText",
            "text": data,
        }


    def respond(self,**kwargs):
        return json.dumps(self.json,indent=2,**kwargs)




@root.route('/', methods=["HEAD","GET","POST"])
def appliaction():
    if request.method in ["HEAD","GET"]:
        return "alive"
    elif request.method == "POST":

        data = json.loads(request.data.decode())
        print("========================================request========================================")
        print(json.dumps(data,indent=2,ensure_ascii=False))

        handle = Lamp(data)
        handle.load("收到")
        print("========================================respond========================================" ,
              handle.respond(ensure_ascii=False))
        return handle.respond()

    else:
        print(request.method)
        return "error", 404


@root.route('/health')
def healthcheck():
    return "<h1>alive,verison 0.1.0</h1>"