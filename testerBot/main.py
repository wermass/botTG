import telebot
from telebot import types
from game import my_game

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)

# переменные камня
y = 'камень'
y1 = '🪨'
#переменные ножниц
e = 'ножницы'
e1 = '✂️'
# переменные бумага
r = 'бумага'
r1 = '🧻'


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(content_types='text')
def bot_main(message):
    if message.text.lower() in [y, y1, y+y1, y1+y, e, e1, e+e1, e1+e, r, r1, r+r1, r1+r] :

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('🪨Камень')
        item2 = types.KeyboardButton('✂️Ножницы')
        item3 = types.KeyboardButton('🧻Бумага')
        markup.add(item1, item2, item3)
        my_game(message, bot)
        bot.send_message(message.chat.id,' Продолжим!',   reply_markup=markup)
    else :
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('🪨Камень')
        item2 = types.KeyboardButton('✂️Ножницы')
        item3 = types.KeyboardButton('🧻Бумага')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '''Что бы поиграть в игру-
        Введите камень,ножницы или бумага
        (можно смайликами 🪨, ✂️, 🧻).
Введите "сложить Х и У, что бы получить сумму чисел "Х и У"''', reply_markup=markup)


bot.infinity_polling()
