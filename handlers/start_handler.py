from telegram.ext import CommandHandler
import handlers.handler_constants as const
from utils import content
from utils import app_loger

def start(update, context):
    text = content.get_text(const.START, 'hello')
    update.message.reply_text(text)
    app_loger.info(const.START + ": " + text)
    
start_handler = CommandHandler(const.START, start)
