from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #log(update)
    msg = str(update.message.text)
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')