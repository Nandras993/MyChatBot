import openai
import json


class Chatbot:
    def __init__(self):
        path = "configuration.json"

        with open(path, "r") as handler:
            info = json.load(handler)

        self.api = info["API"]
        openai.api_key = self.api

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5,
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about music.")
    print(response)
