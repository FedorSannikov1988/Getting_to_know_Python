from pathlib import Path
from bot_commands import *

file_name = "token.config"
relative_file_directory = Path(file_name)

with open(relative_file_directory, 'r') as data:
    my_token = data.read().replace('\n', '')

app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command)  )
app.add_handler(CommandHandler("sum", sum_command))

print("server start")
app.run_polling()