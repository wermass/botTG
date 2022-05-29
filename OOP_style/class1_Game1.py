import telebot
from telebot import types
from random import random
import sqlite3
import os.path
import time

API_TOKEN = '5047557999:AAHVO2o8e3pBwKnlKiIdCbGwSse7ycEO9O8'
bot = telebot.TeleBot(API_TOKEN)

tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид

stone = 'камень'
stone_smile = '🪨'
all_stone =[stone, stone_smile, stone + stone_smile, stone_smile + stone]
# переменные ножниц
shear = 'ножницы'
shear_smile = '✂️'
all_shear = [shear, shear_smile, shear + shear_smile, shear_smile + shear]
# переменные бумага
paper = 'бумага'
paper_smile = '🧻'
all_paper = [paper, paper_smile, paper + paper_smile, paper_smile + paper]

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
stone_button = types.KeyboardButton('🪨Камень')
shear_button = types.KeyboardButton('✂️Ножницы')
paper_button = types.KeyboardButton('🧻Бумага')
markup.add(stone_button, shear_button, paper_button)




class Tester:

    def start1(self, message):
        # self.arg = arg
        print(message)
        bot.send_message(message.chat.id, 'Приветствую! выбери, что ты покажешь!')

    def my_game1(self, message):
        comp_move = int(random() * 3)
        user_id = message.from_user.id
        if not os.path.exists('itproger.db'):
            print('Error not file')  # можно создать
        db = sqlite3.connect('itproger.db')  # создаем таблицу с именем в скобках
        player = 0
        comp = 0
        # создаем курсор
        cur = db.cursor()
        login_player = cur.execute("SELECT id FROM CHEK WHERE id = ?", (user_id,)).fetchone()
        # print('login_player', login_player)
        if login_player is None:
            cur.execute("INSERT INTO CHEK VALUES(?,?, ?)", (user_id, comp, player))
        else:
            znachenia = cur.execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user_id,)).fetchone()
            # print('znachenia    ', znachenia)
            comp = int(znachenia[0])
            player = int(znachenia[1])
            # print('компьютер   ', comp, type(comp))
            # print('игрок       ', player, type(player))
            sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
            data = (comp, player, user_id)
            cur.execute(sql_update_query, data)
            db.commit()




        # начинаю воротить со второй 'events' таблицей в базе 'itproger.db'
        cur.execute("""CREATE TABLE IF NOT EXISTS events(
           Numbers_move INT PRIMARY KEY,
           ID_Player int, 
           date DATE,  
           showed_player TEXT, 
           showed_comp TEXT, 
           total_C_P TEXT); 
        """)
        db.commit()

        # определяем в переменную, что показал игрок, что показал комп, классом я думаю это было бы удобнее
        player_showed = ''
        if message.text.lower() in all_stone:
            player_showed = stone
        elif message.text.lower() in all_stone:
            player_showed = shear
        else:
            player_showed = paper

        comp_showed = ''
        if comp_move == 0:
            comp_showed = stone
        elif comp_move == 1:
            comp_showed = shear
        else:
            comp_showed = paper
        total_events = f'comp: {str(comp)}  player: {str(player)}'
        sqlite_insert_with_param = """INSERT INTO events
                                      (ID_Player, date, showed_player, showed_comp, total_C_P)
                                      VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (user_id, tconv(message.date), player_showed, comp_showed, total_events)
        cur.execute(sqlite_insert_with_param, data_tuple)

        db.commit()

        # короче, какого-то хуя не работает INTEGER PRIMARY KEY в столбце Numpers_move, везде NULL, чутка погуглил,
        # пишут про стандарты, что беда с MySQL
        # я "костылем" через += 1 могу сделать подсчет, но это же должно быть автоматом

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



            elif message.text.lower() in [shear, shear_smile, shear + shear_smile,
                                          shear_smile + shear]:  ### #  win comp[0]
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



            elif message.text.lower() in [paper, paper_smile, paper + paper_smile,
                                          paper_smile + paper]:  ### #  win player[1]
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
            if message.text.lower() in [stone, stone_smile, stone + stone_smile,
                                        stone_smile + stone]:  ### #  win player[1]
                player += 1
                cur = db.cursor()
                sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
                data = (comp, player, user_id)
                cur.execute(sql_update_query, data)
                db.commit()
                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы выйграли! {check}',
                                 reply_markup=markup)

                return player




            elif message.text.lower() in [shear, shear_smile, shear + shear_smile, shear_smile + shear]:  ### #

                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, у вас ничья. {check}',
                                 reply_markup=markup)




            elif message.text.lower() in [paper, paper_smile, paper + paper_smile,
                                          paper_smile + paper]:  ### #  win comp[0]
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
            if message.text.lower() in [stone, stone_smile, stone + stone_smile,
                                        stone_smile + stone]:  ### #  win comp[1]
                comp += 1
                cur = db.cursor()
                sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
                data = (comp, player, user_id)
                cur.execute(sql_update_query, data)
                db.commit()
                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы проиграли. {check}',
                                 reply_markup=markup)

                return comp



            elif message.text.lower() in [shear, shear_smile, shear + shear_smile,
                                          shear_smile + shear]:  ### #  win player[0]
                player += 1
                cur = db.cursor()
                sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
                data = (comp, player, user_id)
                cur.execute(sql_update_query, data)
                db.commit()
                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы выйграли! {check}',
                                 reply_markup=markup)

                return player


            elif message.text.lower() in [paper, paper_smile, paper + paper_smile, paper_smile + paper]:  ### #

                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, у вас ничья. {check}',
                                 reply_markup=markup)

# class Game