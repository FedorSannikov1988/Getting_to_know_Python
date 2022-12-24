from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import functions_for_sql as sql
from pathlib import Path
import text_parsing as t_p
import logger

file_name = "telephone_directory.sqlite"
relative_file_directory = Path(file_name)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    text1 = "Вы зашли в телефонный справочник\n"
    text2 = "/help -> вызов справочного меню\n"
    await update.message.reply_text(f'{text1+text2}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    text1 = "/find_by_name -> найти запись по имени\n"
    text2 = "Пример: /find_by_name Имя\n"
    text3 = "/find_by_surname -> найти запись по фамилии\n"
    text4 = "Пример: /find_by_surname Фамилия\n"
    text5 = "/find_by_name_and_surname -> найти запись по имени и фамилии\n"
    text6 = "Пример: /find_by_name_and_surname Имя Фамилия\n"
    text7 = "/find_by_phone_number -> найти запись по номеру телефона\n"
    text8 = "Пример: /find_by_phone_number номер телефона\n"
    text9 = "/show_all_record -> вывести все записи в справочнике (подумай стоит ли это делать)\n"
    text10 = "/add_entry_phone_book -> добавить запись в телефонную книгу\n"
    text11 = "Пример: /add_entry_phone_book Имя Фамилия номер телефона\n"
    text12 = "/delete_record_in_phone_book -> удалить запись в телефонной книге\n"
    text13 = "Пример: /delete_record_in_phone_book Имя Фамилия\n"
    await update.message.reply_text(f'{text1+text2+text3+text4+text5+text6+text7+text8+text9+text10+text11+text12+text13}')

async def find_by_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    global relative_file_directory
      
    message = str(update.message.text)

    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_name")

    sql_request = '''SELECT people.name, people.surname, phones.phone_number 
    FROM people LEFT JOIN phones ON 
    people.id = people_id WHERE name = "{}"'''.format(message)

    connection = sql.create_connection(relative_file_directory)

    ansver_sql = sql.execute_read_query(connection, sql_request)

    ansver = t_p.print_answer_for_bot_v2(ansver_sql)

    await update.message.reply_text(ansver)

async def find_by_surname(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)
    
    global relative_file_directory
    
    message = str(update.message.text)

    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_surname")

    sql_request = '''SELECT people.name, people.surname, phones.phone_number 
    FROM people LEFT JOIN phones ON
    people.id = people_id WHERE surname = "{}"'''.format(message)

    connection = sql.create_connection(relative_file_directory)

    ansver_sql = sql.execute_read_query(connection, sql_request)

    ansver = t_p.print_answer_for_bot_v2(ansver_sql)

    await update.message.reply_text(ansver)

async def find_by_name_and_surname(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    global relative_file_directory
    
    message = str(update.message.text)

    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_name_and_surname")

    message = message.split(" ")

    sql_request = '''SELECT people.name, people.surname, phones.phone_number FROM people, phones 
    WHERE people.id = people_id AND name = "{}" AND surname = "{}"'''.format(message[0], message[1])
    
    connection = sql.create_connection(relative_file_directory)

    ansver_sql = sql.execute_read_query(connection, sql_request)

    ansver = t_p.print_answer_for_bot_v2(ansver_sql)

    await update.message.reply_text(ansver)

async def find_by_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    global relative_file_directory
 
    message = str(update.message.text)

    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_phone_number")

    sql_request = '''SELECT people.name, people.surname, phones.phone_number 
    FROM phones INNER JOIN people ON phones.people_id = people.id WHERE phone_number = "{}"'''.format(message)

    connection = sql.create_connection(relative_file_directory)
    
    ansver_sql = sql.execute_read_query(connection, sql_request)

    ansver = t_p.print_answer_for_bot_v2(ansver_sql)

    await update.message.reply_text(ansver)

async def show_all_record(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    global relative_file_directory
    
    sql_search_request = '''SELECT people.name, people.surname, phones.phone_number 
    FROM phones INNER JOIN people ON people.id = phones.people_id'''

    connection = sql.create_connection(relative_file_directory)

    ansver_sql = sql.execute_read_query(connection, sql_search_request)

    ansver = t_p.print_answer_for_bot_v2(ansver_sql)

    await update.message.reply_text(ansver)

async def add_entry_phone_book(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    global relative_file_directory
    
    connection = sql.create_connection(relative_file_directory)
    
    message = str(update.message.text)

    message = t_p.clearing_line_from_bot_telegrams(message, "/add_entry_phone_book")

    message = message.split(" ")

    sql_request_for_search = '''SELECT people.name, people.surname, phones.phone_number 
    FROM people LEFT JOIN phones ON people.id = people_id 
    WHERE name = "{}" AND surname = "{}" AND phone_number = "{}" '''.format(message[0], message[1], message[2])

    ansver_sql_for_request_search = sql.execute_read_query(connection, sql_request_for_search)

    if ansver_sql_for_request_search == []:
        sql_request_for_add_human = '''INSERT INTO people (name, surname) 
        VALUES ('{}', '{}') '''.format(message[0], message[1])
        sql.execute_query(connection, sql_request_for_add_human)
        
        sql_request_for_id_add_human = '''SELECT people.id FROM people 
        WHERE name = "{}" AND surname = "{}" '''.format(message[0], message[1])
        id_add_human = sql.execute_read_query(connection, sql_request_for_id_add_human)[0][0]

        sql_request_for_add_phone_number = '''INSERT INTO phones (phone_number, people_id)
        VALUES ('{}', '{}') '''.format(message[2], id_add_human)
        sql.execute_query(connection,  sql_request_for_add_phone_number)

        ansver = "запись добавлена в телефонную книгу"
    else:
        ansver = "данная запись уже существует в телефонной книге"

    await update.message.reply_text(ansver)

async def delete_record_in_phone_book(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    global relative_file_directory
    
    connection = sql.create_connection(relative_file_directory)
    
    message = str(update.message.text)

    message = t_p.clearing_line_from_bot_telegrams(message, "/delete_record_in_phone_book")

    message = message.split(" ")

    sql_request_for_search = '''SELECT people.name, people.surname
    FROM people WHERE name = "{}" AND surname = "{}" '''.format(message[0], message[1])

    ansver_sql_for_request_search = sql.execute_read_query(connection, sql_request_for_search)

    if ansver_sql_for_request_search != []:
        sql_request_for_id_delete_human = '''SELECT people.id FROM people 
        WHERE name = "{}" AND surname = "{}" '''.format(message[0], message[1])
        id_delete_human = sql.execute_read_query(connection, sql_request_for_id_delete_human)[0][0]

        sql_request_for_delete_human_phone_number = '''DELETE FROM phones WHERE people_id = '{}' '''.format(id_delete_human)
        sql.execute_query(connection, sql_request_for_delete_human_phone_number)
        
        sql_request_for_delete_human = '''DELETE FROM people WHERE id = '{}' '''.format(id_delete_human)
        sql.execute_query(connection, sql_request_for_delete_human)

        ansver = "запись удалена из телефонной книги"
    else:
        ansver = "такой записи нет в телефонной книге"

    await update.message.reply_text(ansver)