'''
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
'''

from bot_commands import *

app = ApplicationBuilder().token("5661749736:AAEr_Le1dRoOnJ9sQoZRkwAbV4oAsTTsApM").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command)  )
app.add_handler(CommandHandler("sum", sum_command))

print("server start")
app.run_polling()