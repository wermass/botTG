import telebot
from class1_Game1 import Game_bot
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


V1 = Game_bot('itproger.db')


@bot.message_handler(commands=['start'])
def start(message):
    V1.start1(message)


@bot.message_handler(content_types='text')
def my_game(message):
    V1.my_game1(message)


bot.infinity_polling()
