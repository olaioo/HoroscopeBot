import config_telegram
from telegram import Update
from flask import Flask, request
import configparser
import json

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

#inicia telegram
update_queue, dispatcher, bot = config_telegram.setup()

@app.route('/' + config['TELEGRAM']['BOT_TOKEN'], methods = ['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    update_queue.put(update)
    return ""


if __name__ == '__main__':


    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)