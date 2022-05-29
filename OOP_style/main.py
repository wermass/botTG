import telebot
from class1_Game1 import Tester

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)

V1 = Tester()


@bot.message_handler(commands=['start'])
def start(message):
    V1.start1(message)


@bot.message_handler(content_types='text')
def my_game(message):
    V1.my_game1(message)


bot.infinity_polling()
