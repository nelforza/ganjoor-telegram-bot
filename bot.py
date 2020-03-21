#!/bin/python3

import logging
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from poets_glossary import poets_name_glossary


# Logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Start button command
def start(update, context):
    welcome = 'اسم شاعر مورد نظرت رو بنویس تا بیت شعری ازش تقدیم کنیم'
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome)

def poem(update, context):
    chatID = update.effective_chat.id
    text = 'شاعری با این اسم پیدا نشد!'
    msg = update.message.text
    if msg in poets_name_glossary.values() == False:
        context.bot.send_message(chat_id=chatID, text=text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    ####  Starting the bot ####

    # creates Updater and passes TOKEN
    updater = Updater(token='1084520890:AAHVKkTuWSTLMAfzy7J87zVm8vvDWKo2fKg', use_context=True)
    
    # Getting dispatcher to register handlers
    dp = updater.dispatcher

    # Registering my functions
    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(Filters.text, poem)

    dp.add_handler(msg_handler)
    dp.add_handler(start_handler)

    # Registering Error fuctions
    dp.add_error_handler(error)
    
    # Starts BOT
    updater.start_polling()

    # Keep it active untile CTRL + C
    updater.idle()

if __name__ == "__main__":
    main()
