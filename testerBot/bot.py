import telebot
from telebot import types

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)




# тут я попытался сделать словарь, который будет после команды /start добавлять по ключ "user"(по умолчанию пустая строка) со значением "х", 
# где ключ - это айди чата, а х = 0,но с каждой командой старт становился +1.
# то есть по задумке он из каждого чата добавляет уникальный ключ (айди) в словарь со значением 0.
# при следующей команде /start он видит в библиотеке этот ключ и обновляет его значение на +1
# но как всегда выходит какая-то шняга, он вбивает сначала в словарь ключ с айди (5124962240) со значением 0,
# но со второй команды старт KeyError: 5124962240,я так понимаю он не находит ключ.

user = ''
x = 0
test = {
}


@bot.message_handler(commands=['start'])
def start(message):

  global x
  global user
  global test
  
  user = message.from_user.id
  if test.keys() in [user]:
  
    bot.send_message(message.chat.id, '123')
    x+=1
    return test.update({user: x})
    
    
  else:
        return test.update({user: x}) 
     
  
  
  
  
  

  
  
  
  
  
  
  
  


@bot.message_handler(content_types='text')
def bot_main(message):
    if message.text.lower() in '1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('1')
        markup.add(item1)
        bot.send_message(message.chat.id,' Продолжим!',   reply_markup=markup)
        
    else :
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('🪨Камень')
        item2 = types.KeyboardButton('✂️Ножницы')
        item3 = types.KeyboardButton('🧻Бумага')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '''Что бы поиграть в игру-
        Нажмите на кнопки 🪨камень,✂️ножницы или 🧻бумага
Введите "сложить Х и У, что бы получить сумму чисел "Х и У"''', reply_markup=markup)


bot.infinity_polling()
