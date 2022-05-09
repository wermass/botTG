import telebot
from telebot import types
import xlswriter
import datetime as dt
count = 1
workbook = xlswriter.Workbook('messages.xlsx')
worksheet = workbook.add_workcheet()

worksheet.write(0, 0, 'Дата')
worksheet.write(0, 1, 'Время')
worksheet.write(0, 2, 'Вид сообщения')
worksheet.write(0, 3, 'Отправитель')
worksheet.write(0, 4, 'ID отправителя')
worksheet.write(0, 5, 'Сообщение и id стикера')
worksheet.write(0, 6, 'Эмоция стикера')
API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    global count
    if message_content_type == 'text':
        if message.text != 'стоп':
            worksheet.write(count, 0, str(dt.datetime.now().date()))
            worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
            worksheet.write(count, 2, 'текст')
            worksheet.write(count, 3, message.from_user.first_name + ' ' + message.from_user.last_name)
            worksheet.write(count, 4, message.from_user.id)
            worksheet.write(count, 5, message.text)
            count += 1
        else:
            workbook.close()
            
            
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):            
    print(message)
    global count
    if message_content_type == 'sticker':
        if message.text != 'стоп':
            worksheet.write(count, 0, str(dt.datetime.now().date()))
            worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
            worksheet.write(count, 2, 'sticker')
            worksheet.write(count, 3, message.from_user.first_name + ' ' + message.from_user.last_name)
            worksheet.write(count, 4, message.from_user.id)
            worksheet.write(count, 5, message.text)
            count += 1
        else:
            workbook.close()



    
bot.infinity_polling(none_stop = True)