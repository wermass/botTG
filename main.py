#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from random import random
API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'

bot = telebot.TeleBot(API_TOKEN)
last_message = ''

# переменные камня
y = 'камень'
y1 = '🪨'
#переменные ножниц
e = 'ножницы'
e1 = '✂️'
# переменные бумага
r = 'бумага'
r1 = '🧻'
@bot.message_handler(func=lambda message: True) 
def bot_main(message):
    if message.text.lower()[0:7] == 'сложить':
        my_sum(message)
    elif message.text.lower() in [y, y1] :
        my_game(message)
    elif message.text.lower() in [e, e1] :
        my_game(message)
    elif message.text.lower() in [r, r1] :   
        my_game(message)
    else :
        bot.send_message(message.chat.id, '''Что бы поиграть в игру-
        Введите камень,ножницы или бумага
        (можно смайликами 🪨, ✂️, 🧻).
Введите "сложить Х и У, что бы получить сумму чисел "Х и У"''')
def my_game(message):    
    x=int(random()*3)
    check_comp = 0
    check_player = 0
    

    if x == 0:
        if message.text.lower()  in [y, y1] :
        
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал камень🪨, у вас ничья. {check}')
                
        elif message.text.lower() in [e, e1] :  
            check_comp +=1
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал камень🪨, вы проиграли. {check}')
            
            return check_comp
        
        elif message.text.lower() in [r, r1] :
            check_player +=1
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал камень🪨, вы выйграли! {check}')
            
            return check_player
                
                
    elif x == 1:
        if message.text.lower()  in [y, y1] :
            check_player +=1
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы выйграли! {check}')
            
            return check_player    
            
        elif message.text.lower() in [e, e1] :
        
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, у вас ничья. {check}')
        
        elif message.text.lower() in [r, r1] :
            check_comp +=1
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы проиграли. {check}')
            
            return check_comp 
                
    elif x == 2:
        if message.text.lower()  in [y, y1] :
            check_comp +=1
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы проиграли. {check}')
            
            return check_comp
                
        elif message.text.lower() in [e, e1] :
            check_player +=1
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы выйграли! {check}')
            
            return check_player
        
        elif message.text.lower() in [r, r1] :
        
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, у вас ничья. {check}')
                
                

            
        
            
 
 
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print('last message', last_message)
    print('One')
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
@bot.message_handler(func=lambda message: True)
def my_sum(message):
    if 'сложить' in message.text.lower()[0:7]:
        chisla = message.text.split()
        chisla_summa = int(chisla[1]) + int(chisla[3])
        bot.send_message(message.chat.id, 'сумма будет '+str(chisla_summa))
        
        

     
        
        
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print('Two')
    print('two1')
    last_message = message.text
    bot.reply_to(message, message.text)


bot.infinity_polling()