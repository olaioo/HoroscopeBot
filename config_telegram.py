from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters
from session_manager import SessionManager
from io import BytesIO
from queue import Queue
from threading import Thread
import configparser
import assistant
import voice
import os


import logging

#configura logging e config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('TelegramBot')

config = configparser.ConfigParser()
config.read('config.ini')


def setup():

    TOKEN = config['TELEGRAM']['BOT_TOKEN']
    PORT = int(os.environ.get('PORT', '8443'))

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    updater.start_webhook(listen='0.0.0.0',
                          port=PORT,
                          url_path=TOKEN)

    #configura webhook
    updater.bot.set_webhook(config['TELEGRAM']['WEBHOOK_URL'] + '/' + config['TELEGRAM']['BOT_TOKEN'])
    updater.idle()

    return (updater, dispatcher)

def start(update, context):
    assistant.validate_session(update.effective_chat.id)
    response_text = assistant.send_message(SessionManager.getInstance().getSession(update.effective_chat.id), '')
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

def message(update, context):
    message_received = update.message.text

    assistant.validate_session(update.effective_chat.id)

    response_text = assistant.send_message(SessionManager.getInstance().getSession(update.effective_chat.id), update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

def receive_voice(update, context):
    assistant.validate_session(update.effective_chat.id)

    audio_file = BytesIO(update.message.voice.get_file().download_as_bytearray())
    text = voice.convert_voice(audio_file)
    response_text = assistant.send_message(SessionManager.getInstance().getSession(update.effective_chat.id), text)
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=voice.convert_text(response_text))