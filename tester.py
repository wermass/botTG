from random import random

# переменные камня
y = 'камень'
y1 = '🪨'
#переменные ножниц
e = 'ножницы'
e1 = '✂️'
# переменные бумага
r = 'бумага'
r1 = '🧻'
def my_game(message):    
    x=int(random()*3)

    if x == 0:
        if message.lower() in [y, y1]:
            print('компьютер показал камень🪨, у вас ничья')
                
        elif message.lower() in [e, e1]:        
            print('компьютер показал камень🪨, вы проиграли')
        
        elif message.lower() in [r, r1]:
            print('компьютер показал камень🪨, вы выйграли!')
                
                
    elif x == 1:
        if message.lower() in [y, y1]:
            print('компьютер показал ножницы✂️, вы выйграли!')
                
        elif message.lower() in [e, e1]:         
            print( 'компьютер показал ножницы✂️, у вас ничья! ')
        
        elif message.lower() in [r, r1]:
            print('компьютер показал ножницы✂️, вы проиграли!')
                
    elif x == 2:
        if message.lower() in [y, y1]:
            print('компьютер показал бумагу🧻, вы проиграли')
                
        elif message.lower()  in [e, e1]:         
            print('компьютер показал бумагу🧻, вы выйграли!')
        
        elif message.lower() in [r, r1]:
            print('компьютер показал бумагу🧻, у вас ничья')

my_game('🧻')