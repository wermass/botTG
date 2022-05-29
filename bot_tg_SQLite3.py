import telebot
from telebot import types
from random import random
# import pickle
import sqlite3


API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)



# db = sqlite3.connect('itproger.db')  # создаем таблицу с именем в скобках
#
# # создаем курсор
# cur = db.cursor()



# with open('check_bots_game.bin', 'rb') as f:
#     data_new = pickle.load(f)  # в эту переменную он загружает всё из файла 'check_bots_game.bin'

# тут я попытался сделать словарь, который будет после команды /start добавлять по ключ "user"(по умолчанию пустая строка) со значением "х",
# где ключ - это айди чата, а х = 0,но с каждой командой старт становился +1.
# то есть по задумке он из каждого чата добавляет уникальный ключ (айди) в словарь со значением 0.
# при следующей команде /start он видит в библиотеке этот ключ и обновляет его значение на +1
# но как всегда выходит какая-то шняга, он вбивает сначала в словарь ключ с айди (5124962240) со значением 0,
# но со второй команды старт KeyError: 5124962240,я так понимаю он не находит ключ.
glupo = 0
user = 0
x = user + 1
test = {
}  # обозначать первым счёт компа, вторым счёт игрока
# test = data_new  # просто приравнял значение словаря к переменной из pickle
# переменные камня
y = 'камень'
y1 = '🪨'
# переменные ножниц
e = 'ножницы'
e1 = '✂️'
# переменные бумага
r = 'бумага'
r1 = '🧻'
# check_comp = 0  # общее количество побед компа
# check_player = 0  # общее количество побед юсера
# data = test  # переменную для словаря, что бы сохранял
# print(data)
# print(data_new)


@bot.message_handler(commands=['start'])
def start(message):
    check_test = 0
    check_test1 = 0
    user = message.from_user.id



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🪨Камень')
    item2 = types.KeyboardButton('✂️Ножницы')
    item3 = types.KeyboardButton('🧻Бумага')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Приветствую! выбери, что ты покажешь!', reply_markup=markup)


@bot.message_handler(content_types='text')
def my_game(message):
    x = int(random() * 3)
    user = message.from_user.id
    global test
    test.setdefault(user, [0, 0])

    # with open('check_bots_game.bin', 'wb') as f:  # сюда сохраняет
    #     pickle.dump(data, f)  # сохраняет 'data' которая == 'test'

    db = sqlite3.connect('itproger.db')  # создаем таблицу с именем в скобках
        # создаем курсор
    cur = db.cursor()
    count1 = 3
    # znachenia = cur.execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user,)).fetchone()
    # print('znachenia    ', znachenia)
    # comp = int(znachenia[0])
    # player = int(znachenia[1])
    # print('компьютер   ', comp, type(comp))
    # print('игрок       ', player, type(player))
    # print('count  ', count1)
    cur.execute("SELECT id FROM CHEK")  # rowid уникальный артикул каждой из записей
    comp = 0
    player = 0
    for i in cur.fetchall():

        if user in i:
            count1 += 1
            print("обновил")
            # return count1
            znachenia = cur.execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user,)).fetchone()
            print('znachenia    ', znachenia)
            comp = int(znachenia[0])
            player = int(znachenia[1])
            print('компьютер   ', comp, type(comp))
            print('игрок       ', player, type(player))
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            break
    if count1 == 3:
        print("добавил")
        cur.execute("INSERT INTO CHEK VALUES(?,?, ?)", (user, comp, player))
        #     print("добавил")

    # znachenia = cur.execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user,)).fetchone()
    # comp = int(znachenia[0])
    # player = int(znachenia[1])
    # print('компьютер   ', comp, type(comp))
    # print('игрок       ', player, type(player))


    # print('база данных   ', prt, type(prt))
    # print('chek komp  ', prt[0], type(prt[0]))
    # print('int chek komp  ', int(prt[0]), type(prt[0]))
    # for i in cur.fetchall():
    #     if user in i:
    #         print(i[0])
    cur.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🪨Камень')
    item2 = types.KeyboardButton('✂️Ножницы')
    item3 = types.KeyboardButton('🧻Бумага')
    markup.add(item1, item2, item3)

    # - замена переменных в чек
    ## - замена переменных + подсчет не чек_*** а тест +=1
    ### - return test[user][0] test[user][1]
    ### # - добавленны кнопки быстрых сообщений
    if x == 0:  ### #
        if message.text.lower() in [y, y1, y + y1, y1 + y]:  ### #

            check = f'''

 Счет компьютер - {comp} Вы - {player}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, у вас ничья. 
{check} ''', reply_markup=markup)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


        elif message.text.lower() in [e, e1, e + e1, e1 + e]:  ### #  win comp[0]
            comp += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f''' 
            
Счет компьютер - {comp} Вы - {player}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы проиграли. 
{check}''', reply_markup=markup)

            return comp

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


        elif message.text.lower() in [r, r1, r + r1, r1 + r]:  ### #  win player[1]
            player += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f''' 

Счет компьютер - {comp} Вы - {player}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы выйграли! 
{check}''', reply_markup=markup)

            return player

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


    elif x == 1:  ### #
        if message.text.lower() in [y, y1, y + y1, y1 + y]:  ### #  win player[1]
            player += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы выйграли! {check}', reply_markup=markup)

            return player

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


        elif message.text.lower() in [e, e1, e + e1, e1 + e]:  ### #

            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, у вас ничья. {check}', reply_markup=markup)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


        elif message.text.lower() in [r, r1, r + r1, r1 + r]:  ### #  win comp[0]
            comp += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы проиграли. {check}',
                             reply_markup=markup)

            return comp

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


    elif x == 2:  ### #
        if message.text.lower() in [y, y1, y + y1, y1 + y]:  ### #  win comp[1]
            comp += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы проиграли. {check}', reply_markup=markup)

            return comp

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


        elif message.text.lower() in [e, e1, e + e1, e1 + e]:  ### #  win player[0]
            player += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы выйграли! {check}', reply_markup=markup)

            return player

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)


        elif message.text.lower() in [r, r1, r + r1, r1 + r]:  ### #

            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, у вас ничья. {check}', reply_markup=markup)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🪨Камень')
            item2 = types.KeyboardButton('✂️Ножницы')
            item3 = types.KeyboardButton('🧻Бумага')
            markup.add(item1, item2, item3)



@bot.message_handler(content_types='text')
def bot_main(message):
    if message.text.lower() in '1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('1')
        markup.add(item1)
        bot.send_message(message.chat.id, ' Продолжим!', reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('🪨Камень')
        item2 = types.KeyboardButton('✂️Ножницы')
        item3 = types.KeyboardButton('🧻Бумага')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '''Что бы поиграть в игру-
        Нажмите на кнопки 🪨камень,✂️ножницы или 🧻бумага
Введите "сложить Х и У, что бы получить сумму чисел "Х и У"''', reply_markup=markup)


bot.infinity_polling()
