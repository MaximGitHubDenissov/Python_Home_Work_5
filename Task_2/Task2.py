# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

def turn():
    while True:
        n = input('Сколько конфет возьмете?: ')
        try:
            n = int(n)
            if 0 < n <= 28 and n <= total:
                break
            else: 
                print('Ваше число неправильное!')
        except: 
            print('Ошибка!!! Нужно вводить числа')
    return n

# 1 вариант - Игра на двоих человек
from random import randint
# print('Привет! Попробуйте поиграть в игру конфеты. Правила в комментариях выше')
# name_one = input('Введите имя первого игрока: ')
# name_two = input('Введите имя второго игрока: ')
# chose = randint(0,1)
# if chose == 0:
#     first = name_one
#     second = name_two
# else:
#     first = name_two
#     second = name_one
# total = 2021
# while total > 0:
#     print('Осталось', total, 'кофет')
#     print(first, 'Ваш ход!')
#     n = turn()
#     total -= n
#     if total == 0:
#         print(first, 'Вы выиграли!')
#         break
#     print('='*10)
#     print('Осталось', total, 'кофет')
#     print(second, 'Ваш ход!')
#     n = turn()
#     total -= n
#     if total == 0:
#         print(second, 'Вы выиграли!')
#         break
#     print('='*10)

# 2 вариант - Игра с ботом

from random import randint
print('Привет! Попробуйте поиграть в игру конфеты. Правила в комментариях выше. Попробуй выиграть бота!')
player_name = input('Введите свое имя: ')
chose = randint(0,1)
total = 2021
if chose == 0:
    print('Первым ходит бот!')
    num = total%29
    total -= num
    print('Бот взял', num, 'конфет')
while total > 0:
    print('Осталось', total, 'кофет')
    print(player_name, 'Ваш ход!')
    n = turn()
    total -= n
    if total == 0:
        print(player_name, 'Вы выиграли!')
        break
    print('='*10)
    print('Осталось', total, 'кофет')
    print('Ход бота!')
    if total%29 == 0:
        num = randint(1,28)
    else:
        num = total%29
    total -= num
    print('Бот взял', num, 'конфет')
    if total == 0:
        print('Бот выиграл!')
        break
    print('='*10)


