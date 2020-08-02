#!/usr/bin/env python

# import os
# os.environ["CONFIGS_PATH"] = 'static/configs/app_config.json'

from utils import config, app_loger
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(config.get_config('telegram_token'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(start_handler) 
    dp.add_handler(help_handler)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    app_loger.info("Main loop>>>")
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
