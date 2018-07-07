from flask import Flask, render_template, request
from chatbot import response
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("./data/intents.yaml")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(response(userText))


if __name__ == "__main__":
    app.run()
