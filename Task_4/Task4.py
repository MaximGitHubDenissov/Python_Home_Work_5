# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# модуль сжатия
working_list = []
path = r'C:\Users\77017\OneDrive\Рабочий стол\Python_Home_Work_5\Task_4\input_data.txt'
with open(path, 'r') as file:
    for line in file:
        working_list.extend(line.strip())
result_list = []
i = 0
while i < len(working_list):
    count = 1
    while i+1 < len(working_list) and working_list[i] == working_list[i+1]:
        count += 1
        i +=1
    result_list.append(working_list[i] + str(count))
    i +=1
path_output = r'C:\Users\77017\OneDrive\Рабочий стол\Python_Home_Work_5\Task_4\output_data.txt'
with open(path_output, 'w') as output_file:
    output_file.write(''.join(result_list))

# модуль восстановления
path_input = r'C:\Users\77017\OneDrive\Рабочий стол\Python_Home_Work_5\Task_4\output_data.txt'
with open(path_output, 'r') as f:
    for line in f:
        my_str = line
result_str = ''        
for i in range(len(my_str)):
    if my_str[i].isdigit():
        result_str += my_str[i-1] * int(my_str[i])
print(result_str)