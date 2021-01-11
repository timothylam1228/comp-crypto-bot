#coding=UTF-8

import logging
import boto3
from botocore.exceptions import ClientError
import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler,StringCommandHandler, InlineQueryHandler
from telegram import InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity, ForceReply, InlineKeyboardButton,InlineKeyboardMarkup,InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.utils import helpers
from telegram.utils.helpers import escape_markdown
import datetime
import os
import json
from uuid import uuid4
import csv
from botocore.config import Config
from io import BytesIO
import requests

#PORT = int(os.environ.get('PORT', 5000))
SO_COOL = 'hkcc-it'


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('/p')


def p(update, context):
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
    print(response)



def main():
    global update_id
    #TOKEN='1588067244:AAGS6SjeUl9yw416K_dH-306392YyKCJepE'
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start,filters=~Filters.group))
    dp.add_handler(CommandHandler("price", p))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int('5000'),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://comp-crypto-bot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()



'''

'''