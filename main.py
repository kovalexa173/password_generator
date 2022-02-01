import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password


def num_is_valid(value):
    while not value.isdigit() or int(value) < 1:
        print("Некорректное значение")
        value = input("Введите число больше нуля")
    return int(value)

def is_valid(value):
    while value.lower() not in "да, нет":
        print("Некорректное значение")
        value = input("Введите да или нет")
    return value.lower()
print("Добро пожаловать в генератор паролей")
count_password = num_is_valid(input("Введите количество желаемых паролей"))
count_symbol = num_is_valid(input("Введите количество символов для пароля"))
add_digit = is_valid(input('Включить цифры? (д = да, н = нет) ')).strip()
add_lowercase = is_valid(input('Включить прописные буквы? (д = да, н = нет) ')).strip()
add_uppercase = is_valid(input('Включить строчные буквы? (д = да, н = нет) ')).strip()
add_punctuation = is_valid(input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ')).strip()
remove_badsymbols = is_valid(input('Исключить символы il1Lo0O? (д = да, н = нет)')).strip()

if add_digit.lower() == 'да':
    chars += digits
if add_lowercase.lower() == 'да':
    chars += lowercase_letters
if add_uppercase.lower() == 'да':
    chars += uppercase_letters
if add_punctuation.lower() == 'да':
    chars += punctuation
if remove_badsymbols.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for _ in range(count_password):
    print(generate_password(count_symbol, chars))