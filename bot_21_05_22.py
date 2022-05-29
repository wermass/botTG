import telebot
from telebot import types
from random import random
import sqlite3
import os.path


API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)

# сделать в базе 2 таблицу, в которой созраняются исходы каждого раунда.
# кто сходил, когда сходил, что показл пользователь, что компьютер, результат хода. (название таблицы events)
# переписать бота, используя ООП
# скачать видосы, набрать код по ООП

stone = 'камень'
stone_smile = '🪨'
# переменные ножниц
shear = 'ножницы'
shear_smile = '✂️'
# переменные бумага
paper = 'бумага'
paper_smile = '🧻'

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
stone_button = types.KeyboardButton('🪨Камень')
shear_button = types.KeyboardButton('✂️Ножницы')
paper_button = types.KeyboardButton('🧻Бумага')
markup.add(stone_button, shear_button, paper_button)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую! выбери, что ты покажешь!', reply_markup=markup)


@bot.message_handler(content_types='text')
def my_game(message):
    comp_move = int(random() * 3)
    user_id = message.from_user.id
    if not os.path.exists('itproger.db'):
        print('Error not file')  # можно создать
    db = sqlite3.connect('itproger.db')  # создаем таблицу с именем в скобках
    # создаем курсор
    player = 0
    comp = 0
    cur = db.cursor()
    login_player = cur.execute("SELECT id FROM CHEK WHERE id = ?", (user_id,)).fetchone()
    print('login_player', login_player)
    if login_player is None:
        cur.execute("INSERT INTO CHEK VALUES(?,?, ?)", (user_id, comp, player))
    else:
        znachenia = cur.execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user_id,)).fetchone()
        print('znachenia    ', znachenia)
        comp = int(znachenia[0])
        player = int(znachenia[1])
        print('компьютер   ', comp, type(comp))
        print('игрок       ', player, type(player))
        sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
        data = (comp, player, user_id)
        cur.execute(sql_update_query, data)
        db.commit()

    cur.close()

    # - замена переменных в чек
    ## - замена переменных + подсчет не чек_*** а тест +=1
    ### - return test[user][0] test[user][1]
    ### # - добавленны кнопки быстрых сообщений
    if comp_move == 0:  ### #
        if message.text.lower() in [stone, stone_smile, stone + stone_smile, stone_smile + stone]:  ### #

            check = f'''

 Счет компьютер - {comp} Вы - {player}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, у вас ничья.
{check} ''', reply_markup=markup)



        elif message.text.lower() in [shear, shear_smile, shear + shear_smile, shear_smile + shear]:  ### #  win comp[0]
            comp += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f'''

Счет компьютер - {comp} Вы - {player}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы проиграли.
{check}''', reply_markup=markup)

            return comp



        elif message.text.lower() in [paper, paper_smile, paper + paper_smile, paper_smile + paper]:  ### #  win player[1]
            player += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f'''

Счет компьютер - {comp} Вы - {player}'''
            bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы выйграли!
{check}''', reply_markup=markup)

            return player



    elif comp_move == 1:  ### #
        if message.text.lower() in [stone, stone_smile, stone + stone_smile, stone_smile + stone]:  ### #  win player[1]
            player += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы выйграли! {check}', reply_markup=markup)

            return player




        elif message.text.lower() in [shear, shear_smile, shear + shear_smile, shear_smile + shear]:  ### #

            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, у вас ничья. {check}', reply_markup=markup)




        elif message.text.lower() in [paper, paper_smile, paper + paper_smile, paper_smile + paper]:  ### #  win comp[0]
            comp += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы проиграли. {check}',
                             reply_markup=markup)

            return comp




    elif comp_move == 2:  ### #
        if message.text.lower() in [stone, stone_smile, stone + stone_smile, stone_smile + stone]:  ### #  win comp[1]
            comp += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы проиграли. {check}', reply_markup=markup)

            return comp



        elif message.text.lower() in [shear, shear_smile, shear + shear_smile, shear_smile + shear]:  ### #  win player[0]
            player += 1
            cur = db.cursor()
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()
            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы выйграли! {check}', reply_markup=markup)

            return player


        elif message.text.lower() in [paper, paper_smile, paper + paper_smile, paper_smile + paper]:  ### #

            check = f' Счет компьютер - {comp} Вы - {player}'
            bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, у вас ничья. {check}', reply_markup=markup)


bot.infinity_polling()
