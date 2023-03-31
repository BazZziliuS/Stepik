# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число. 
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. 
# Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. 
# Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

import random

def is_valid(num):
    try:
        num = int(num)
        if num in range(1, 101):
            return True
        else:
            return False
    except:
        return False
    
print('Добро пожаловать в числовую угадайку')
counter = 0

while True:
    try:
        if is_valid(right_num): pass
    except:
        right_num = input('Введите правую границу от 1 до 100:\n')
        if not is_valid(right_num):
            print('А может быть все-таки введем целое число от 1 до 100?\n')
            continue
        random_num = random.randint(1, int(right_num))

    
    response = input(f'Напиши число от 1 до {right_num}:\n')
    if not is_valid(response):
        print(f'А может быть все-таки введем целое число от 1 до {right_num}?\n')
        continue
    
    response = int(response)
    counter +=1
    
    if response < random_num:
        print('Ваше число меньше загаданного, попробуйте еще разок\n')
    if response > random_num:
        print('Ваше число больше загаданного, попробуйте еще разок\n')
    if response == random_num:
        print(f'Вы угадали с {counter} попытки, поздравляем!\n')
        
        response = input('Повторим игру? (д - да, н - нет)\n')
        if response == 'д':
            random_num = random.randint(1, 101)
            counter = 0
        else:
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')