# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. 
# Она должна запрашивать у пользователя следующие данные:
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).

value_list = list('0123456789')
eng_lower_list = list('abcdefghijklmnopqrstuvwxyz')
eng_upper_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rus_lower_list = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
rus_upper_list = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

def rotate_letter(letter, rotate, letter_list):
    letter_pos = letter_list.index(letter) + rotate
    list_len = len(letter_list)
    letter_pos %= list_len
    return letter_list[letter_pos]

def get_caesar(text: str, rotate: int):
    if len(text) == 0:
        return print("Введённая строка пуста (длина равна нулю)")

    response = ""

    for i in list(text):
        if i in value_list:
            r = rotate_letter(i, rotate, value_list)
        elif i in eng_lower_list:
            r = rotate_letter(i, rotate, eng_lower_list)
        elif i in eng_upper_list:
            r = rotate_letter(i, rotate, eng_upper_list)
        elif i in rus_lower_list:
            r = rotate_letter(i, rotate, rus_lower_list)
        elif i in rus_upper_list:
            r = rotate_letter(i, rotate, rus_upper_list)
        else:
            r = i
        response += r
    return response

print('Приветсвую в шифраторе Цезаря!')
text = input('Введите текст: ')
step = input('Введите шаг вправо: ')
decode = input('Шифрование или дешифрование (ш, д): ')
if decode == 'д': step = '-' + step
print('Результат:', get_caesar(str(text), int(step)))