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

check_comp = 0
check_player = 0



def my_game(message, bot):    
    x=int(random()*3)
    
    global check_comp
    global check_player
    
    
    if x == 0:
        if message.text.lower()  in [y, y1, y+y1, y1+y] :
        
            check = f' Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал камень🪨, у вас ничья. \n {check} ')
            
        elif message.text.lower() in [e, e1, e+e1, e1+e] :  
            check_comp +=1
            check = f'Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал камень🪨, вы проиграли. \n {check}')
            
            return check_comp
        
        elif message.text.lower() in [r, r1, r+r1, r1+r] :
            check_player +=1
            check = f'Счет компьютер - {check_comp} Вы - {check_player}'
            bot.send_message(message.chat.id, f'компьютер показал камень🪨, вы выйграли! \n {check}')
            
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
 
