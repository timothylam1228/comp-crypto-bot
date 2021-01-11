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


PORT = int(os.environ.get('PORT', 5000))
SO_COOL = 'hkcc-it'


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('/source for Geting the source\n/canteen to show canteen')


def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))
    path="https://github.com/timothylam1228/telegram_bot/raw/master/source/"
    file=str(query.data)
    pdf=".pdf"
    jpg=".jpg"
    context.bot.sendDocument(chat_id=query.message.chat.id, document=path+file+pdf)
    if(file=="Maths Diagnostic Test"):
        context.bot.sendPhoto(chat_id=query.message.chat.id, photo='https://github.com/timothylam1228/telegram_bot/raw/master/source/maths_diagonositc_test_changed.jpg')
        context.bot.sendMessage(chat_id=query.message.chat.id,text =" Q7.6 has update Please be careful")


def open_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2021, 1, 25) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    #update.message.reply_text("開左學啦仲倒數 \n用 /endday 睇下幾時完SEM",reply_markup = ReplyKeyboardRemove())
    update.message.reply_text("距離開SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

def end_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2020, 12, 17,12,45) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    #update.message.reply_text("距離完SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")
    update.message.reply_text("完左SEM啦仲倒數 \n用 /openday 睇下幾時開SEM",reply_markup = ReplyKeyboardRemove())

def gpa_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2021, 1, 19) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    update.message.reply_text("距離出GPA仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

def help_command(update, context):
    x = update.message.from_user.id
    update.message.reply_text(x,)




def main():
    global update_id
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    #In source.py
    dp.add_handler(CommandHandler("start", start,filters=~Filters.group))

    #dp.add_handler(CommandHandler("donateToMe",donateToMe,pass_args = True))


    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
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