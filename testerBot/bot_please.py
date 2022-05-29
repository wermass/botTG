import telebot
from telebot import types
from random import random
import pickle


API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)

with open('check_bots_game.bin', 'rb') as f:
    data_new = pickle.load(f)  # в эту переменную он загружает всё из файла 'check_bots_game.bin'


# тут я попытался сделать словарь, который будет после команды /start добавлять по ключ "user"(по умолчанию пустая строка) со значением "х", 
# где ключ - это айди чата, а х = 0,но с каждой командой старт становился +1.
# то есть по задумке он из каждого чата добавляет уникальный ключ (айди) в словарь со значением 0.
# при следующей команде /start он видит в библиотеке этот ключ и обновляет его значение на +1
# но как всегда выходит какая-то шняга, он вбивает сначала в словарь ключ с айди (5124962240) со значением 0,
# но со второй команды старт KeyError: 5124962240,я так понимаю он не находит ключ.

user = 0
x = user + 1
test = {        
}                       # обозначать первым счёт компа, вторым счёт игрока
test = data_new  #  просто приравнял значение словаря к переменной из pickle
# переменные камня
y = 'камень'
y1 = '🪨'
#переменные ножниц
e = 'ножницы'
e1 = '✂️'
# переменные бумага
r = 'бумага'
r1 = '🧻'    
check_comp = 0
check_player = 0
data = test  #  переменную для словаря, что бы сохранял
print(data)
print(data_new)
@bot.message_handler(commands=['start'])
def start(message):
  
  check_test = 0
  check_test1 = 0
  user = message.from_user.id
  for i in test:
    print(i, 'i')
    print(test[i], 'test[i]')
    if i == user:
        check_test += 1
        print(check_test, 'check_test')
        check_test1 += 2
        print(check_test1, 'check_test1')
        test[i][0] += 1
        test[i][1] += 2
        print(test[i][0], 'test[i][0]')
        print(test[i][1], 'test[i][1]')
  test.setdefault(user, [0, 0]) 
  print(user, '(user)')
  print(test, '(test)')
  

@bot.message_handler(content_types='text')
def my_game(message):    
    x=int(random()*3)
    user = message.from_user.id
    global check_comp 
    global check_player
    global test
    test.setdefault(user, [0, 0])
    #test[user][0] = check_comp
    #test[user][1] = check_player        
    #print(check_comp, check_player, "check_comp", 'check_player')
    with open('check_bots_game.bin', 'wb') as f:  # сюда сохраняет 
        pickle.dump(data, f)  #  сохраняет 'data' которая == 'test'
    print(test, 'test')
    
    
    
    
    # - замена переменных в чек
    ## - замена переменных + подсчет не чек_*** а тест +=1
    ### - return test[user][0] test[user][1]
    if x == 0:  ###
        if message.text.lower()  in [y, y1, y+y1, y1+y] :  ###
        
            check = f'''

 Счет компьютер - {test[user][0]} Вы - {test[user][1]}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, у вас ничья. 
{check} ''')
            
        elif message.text.lower() in [e, e1, e+e1, e1+e] :  ###  win comp[0]
            test[user][0] +=1
            check = f''' 

Счет компьютер - {test[user][0]} Вы - {test[user][1]}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы проиграли. 
{check}''')
            
            return test[user][0]
        
        elif message.text.lower() in [r, r1, r+r1, r1+r] :  ### win player[1]
            test[user][1] +=1
            check = f''' 

Счет компьютер - {test[user][0]} Вы - {test[user][1]}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы выйграли! 
{check}''')
            
            return test[user][1]
                
                
    elif x == 1:  ###
        if message.text.lower()  in [y, y1, y+y1, y1+y] :  ### win player[1]
            test[user][1] +=1
            check = f' Счет компьютер - {test[user][0]} Вы - {test[user][1]}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы выйграли! {check}')
            
            return test[user][1]    
            
        elif message.text.lower() in [e, e1, e+e1, e1+e] :  ###
        
            check = f' Счет компьютер - {test[user][0]} Вы - {test[user][1]}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, у вас ничья. {check}')
        
        elif message.text.lower() in [r, r1, r+r1, r1+r] :  ### win comp[0]
            test[user][0] +=1
            check = f' Счет компьютер - {test[user][0]} Вы - {test[user][1]}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы проиграли. {check}')
            
            return test[user][0] 
                
    elif x == 2:  #
        if message.text.lower()  in [y, y1, y+y1, y1+y] :  ### win comp[1]
            test[user][0] +=1
            check = f' Счет компьютер - {test[user][0]} Вы - {test[user][1]}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы проиграли. {check}')
            
            return test[user][0]
                
        elif message.text.lower() in [e, e1, e+e1, e1+e] :  ### win player[0]
            test[user][1] +=1
            check = f' Счет компьютер - {test[user][0]} Вы - {test[user][1]}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы выйграли! {check}')
            
            return test[user][1]
        
        elif message.text.lower() in [r, r1, r+r1, r1+r] :  ###
        
            check = f' Счет компьютер - {test[user][0]} Вы - {test[user][1]}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, у вас ничья. {check}')




  
  

  
  
  
  
  
  
  
  


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
