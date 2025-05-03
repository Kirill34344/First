import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''


n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? ').strip()
add_lowercase = input('Включить прописные буквы? ')
add_uppercase = input('Включить строчные буквы? ')
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? ')
remove_badsymbols = input('Исключить символы il1Lo0O? ')


if add_digit.lower() == 'y':
    chars += digits
if add_lowercase.lower() == 'y':
    chars += lowercase_letters
if add_uppercase.lower() == 'y':
    chars += uppercase_letters
if add_punctuation.lower() == 'y':
    chars += punctuation
if remove_badsymbols.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password


for _ in range(n):
    print(generate_password(length, chars))