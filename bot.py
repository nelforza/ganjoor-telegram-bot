#!/bin/python3

import logging
import sqlite3
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from poets_names import poets_fullnames_dic, poets_names_list
from verse_query import query
from msg_poem import msg_poem
from msg_for_user import slash_N
from command_validate import is_valid

# Logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Error logging
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Start button command
def start(update, context):
    chatID = update.effective_chat.id
    welcome = 'کافیه اسم شاعرِ مورد نظرتون رو بنویسید تا بیتِ شعری از اون شاعر تقدیم کنیم.'
    commands = 'دستور /commands بهت کمک می‌کنه تا لیست دستورات موجود رو ببینی'
    context.bot.send_message(chat_id=chatID, text=welcome+'\n'+commands)

def about(update, context):
    chatID = update.effective_chat.id
    url = 'https://github.com/nelforza/ganjoor-telegram-bot'
    text = '''
    این ربات توسط حسین حیدری و به زبان پایتون نوشته شده و تحت لایسنس آزاد GPL منتشر شده است.


اگر ایده‌ای دارید که بشه بهش اضافه کرد: @addones
لینک به ریپو گیت‌هاب:
    '''
    context.bot.send_message(chat_id=chatID, text=text+'\n'+url)

def commands(update, context):
    chatID = update.effective_chat.id
    text = '''ریپو کد:
/about
متن شروع:
/start
لیست شاعران:
/poets
برای همین پیام که الان می‌بینید :)
/commands'''
    context.bot.send_message(chat_id=chatID, text=text)


def poets(update, context):
    chatID = update.effective_chat.id
    poets = ''
    # searches in poets dictionary and provides it's values which are poets names in Persian
    for value in poets_fullnames_dic.values():
        poets += str(value)+'\n'
    context.bot.send_message(chat_id=chatID, text=poets)


def poem(update, context):
    
    chatID = update.effective_chat.id
    msg = update.message.text

    if is_valid(msg) == False:
        pass
    else:
        msg, length = is_valid(msg)
        # checking if the user's message is really a poet name 
        if msg not in poets_names_list:
            not_found_text = 'شاعری با این اسم پیدا نشد!'
            context.bot.send_message(chat_id=chatID, text=not_found_text)
        else:
            if length == 'long':
                poem = msg_poem(msg, length)
                if len(poem) > 90:
                    main_part = poem[:90]
                    rest = len(poem) - 90
                    second_part = poem[-rest:]
                
                    main_part_to_send, second_part_to_send = slash_N(main_part=main_part, second_part=second_part)
                    context.bot.send_message(chat_id=chatID, text=main_part_to_send)
                    context.bot.send_message(chat_id=chatID, text=second_part_to_send)
            elif length == 'short':
                poem = msg_poem(msg, length)
                message_to_send = slash_N(main_part=poem)
                context.bot.send_message(chat_id=chatID, text=message_to_send)




def main():
    ####  Starting the bot ####

    # creates Updater and passes TOKEN
    updater = Updater(token='1084520890:AAFzlyspcYYZhW0D6yN0n-1zUEOaHM1dopo', use_context=True)
    
    # Getting dispatcher to register handlers
    dp = updater.dispatcher

    # Registering my functions
    start_handler = CommandHandler('start', start)
    poets_handler = CommandHandler('poets', poets)
    about_handler = CommandHandler('about', about)
    command_handler = CommandHandler('commands', commands)
    msg_handler = MessageHandler(Filters.text, poem)

    dp.add_handler(start_handler)
    dp.add_handler(poets_handler)
    dp.add_handler(about_handler)
    dp.add_handler(command_handler)
    dp.add_handler(msg_handler)


    # Registering Error fuctions
    dp.add_error_handler(error)
    
    # Starts BOT
    updater.start_polling()

    # Keep it active untile CTRL + C
    updater.idle()

if __name__ == "__main__":
    main()


