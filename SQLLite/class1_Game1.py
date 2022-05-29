import telebot
from telebot import types
from random import random
import sqlite3
import os.path
import time
from config import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


# вытащить весь SQL в класс Game_db

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




class Game_bot:

    def __init__(self, db_name):
        self.db_name = db_name
        self.game_db = Game_db(db_name)

    def start1(self, message):
        # self.arg = arg
        print(message)
        bot.send_message(message.chat.id, 'Приветствую! выбери, что ты покажешь!')

    def my_game1(self, message):
        comp_move = int(random() * 3)
        user_id = message.from_user.id
        player = 0
        comp = 0
        self.game_db.connect()
        # создаем курсор
        cur = self.game_db.sqlite.cursor()
        login_player = self.game_db.find_user(user_id)
        # print('login_player', login_player)
        if login_player is None:
            self.game_db.create_user(user_id, comp, player)
        else:
            comp = self.game_db.opredelitb_znachenia_comp(user_id)
            player= self.game_db.opredelitb_znachenia_player(user_id)
            self.game_db.update_chek(comp, player, user_id)

        # начинаю воротить со второй 'events' таблицей в базе 'itproger.db'
        self.game_db.create_db()

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

        self.game_db.update_events(user_id, tconv(message.date), player_showed, comp_showed, total_events)

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
                self.game_db.update_chek(comp, player, user_id)
                check = f'''

    Счет компьютер - {comp} Вы - {player}'''
                bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы проиграли.
    {check}''', reply_markup=markup)

                return comp



            elif message.text.lower() in [paper, paper_smile, paper + paper_smile,
                                          paper_smile + paper]:  ### #  win player[1]
                player += 1
                self.game_db.update_chek(comp, player, user_id)
                check = f'''

    Счет компьютер - {comp} Вы - {player}'''
                bot.send_message(message.chat.id, f'''компьютер показал камень🪨, вы выйграли!
    {check}''', reply_markup=markup)

                return player



        elif comp_move == 1:  ### #
            if message.text.lower() in [stone, stone_smile, stone + stone_smile,
                                        stone_smile + stone]:  ### #  win player[1]
                player += 1
                self.game_db.update_chek(comp, player, user_id)
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
                self.game_db.update_chek(comp, player, user_id)
                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал ножницы✂️, вы проиграли. {check}',
                                 reply_markup=markup)

                return comp




        elif comp_move == 2:  ### #
            if message.text.lower() in [stone, stone_smile, stone + stone_smile,
                                        stone_smile + stone]:  ### #  win comp[1]
                comp += 1
                self.game_db.update_chek(comp, player, user_id)
                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы проиграли. {check}',
                                 reply_markup=markup)

                return comp



            elif message.text.lower() in [shear, shear_smile, shear + shear_smile,
                                          shear_smile + shear]:  ### #  win player[0]
                player += 1
                self.game_db.update_chek(comp, player, user_id)
                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, вы выйграли! {check}',
                                 reply_markup=markup)

                return player


            elif message.text.lower() in [paper, paper_smile, paper + paper_smile, paper_smile + paper]:  ### #

                check = f' Счет компьютер - {comp} Вы - {player}'
                bot.send_message(message.chat.id, f'компьютер показал бумагу🧻, у вас ничья. {check}',
                                 reply_markup=markup)

class Game_db:

    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        if not os.path.exists(self.db_name):
            print('Error not file')  # можно создать
        self.sqlite = sqlite3.connect(self.db_name)  # создаем таблицу с именем в скобках

    def find_user(self, user_id):
        '''
        найти пользователя по user_id
        '''
        return self.sqlite.cursor().execute("SELECT id FROM CHEK WHERE id = ?", (user_id,)).fetchone()

    def create_user(self, user_id, comp, player):
        '''
        Создает нового юзера
        :param user_id:
        :param comp:
        :param player:
        '''
        self.sqlite.cursor().execute("INSERT INTO CHEK VALUES(?,?, ?)", (user_id, comp, player))

    def create_db(self):
        '''
        создаем таблицу в базе при первом запуске
        :return:
        '''
        self.sqlite.execute("""CREATE TABLE IF NOT EXISTS events(
                   Numbers_move INT PRIMARY KEY,
                   ID_Player int, 
                   date DATE,  
                   showed_player TEXT, 
                   showed_comp TEXT, 
                   total_C_P TEXT); 
                """)
        self.sqlite.commit()

    def update_chek(self, comp, player, user_id):
        """
        обновляем таблитцу CHEK
        :param comp:
        :param player:
        :param user_id:
        :return:
        """
        cur = self.sqlite.cursor()
        sql_update_query = """UPDATE CHEK SET chek_comp = ?, chek_player = ? WHERE id = ?"""
        data = (comp, player, user_id)
        cur.execute(sql_update_query, data)
        self.sqlite.commit()

    def update_events(self, user_id, message_date, player_showed, comp_showed, total_events):
        '''
        обновляем таблицу events
        :param user_id:
        :param message_date:
        :param player_showed:
        :param comp_showed:
        :param total_events:
        :return:
        '''
        sqlite_insert_with_param = """INSERT INTO events
                                      (ID_Player, date, showed_player, showed_comp, total_C_P)
                                      VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (user_id, message_date, player_showed, comp_showed, total_events)
        self.sqlite.cursor().execute(sqlite_insert_with_param, data_tuple)

        self.sqlite.commit()

    def opredelitb_znachenia_comp(self, user_id):
        '''
        Определяет счёт компа
        :param user_id:
        :return:
        '''
        znachenia = self.sqlite.cursor().execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user_id,)).fetchone()
        comp = int(znachenia[0])
        return comp

    def opredelitb_znachenia_player(self, user_id):
        '''
        Определяет значения игрока
        :param user_id:
        :return:
        '''
        znachenia = self.sqlite.cursor().execute("SELECT chek_comp, chek_player FROM CHEK WHERE id = ?", (user_id,)).fetchone()
        player = int(znachenia[1])
        return player
