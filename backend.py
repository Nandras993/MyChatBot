import openai
import json



class Chatbot:
    def __init__(self):
        path = "configuration.json"

        with open(path, "r") as handler:
            info = json.load(handler)

        self.api = info["API"]
        openai.api_key = self.api
