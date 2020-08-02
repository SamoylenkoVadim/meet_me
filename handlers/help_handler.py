from telegram.ext import CommandHandler
import handlers.handler_constants as const
from utils import content
from utils import app_loger

def help(update, context):
    text = content.get_text(const.HELP, 'help')
    update.message.reply_text(text)
    app_loger.info(const.HELP + ": " + text)

help_handler = CommandHandler(const.HELP, help)
