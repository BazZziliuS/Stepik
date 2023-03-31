# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
digit = input('Включить цифры? (д = да, н = нет) ').strip()
lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет) ').strip()


if digit.lower() == 'д':
    chars += digits
if lowercase.lower() == 'д':
    chars += lowercase_letters
if uppercase.lower() == 'д':
    chars += uppercase_letters
if punctuation.lower() == 'д':
    chars += punctuation
if badsymbols.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(n):
    print(generate_password(length, chars))