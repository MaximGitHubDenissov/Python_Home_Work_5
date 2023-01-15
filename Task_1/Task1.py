# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_text = 'abc абв ывпвпыро Абв ава ыбв АбВ ываып прок'
my_str = 'абв'
my_list = my_text.split()
res_list = list(filter(lambda x: x.lower() != my_str.lower(), my_list))
print(*res_list)