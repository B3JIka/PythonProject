import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
punc2 = "il1Lo0O"
chars = ''
count = int(input("Количество паролей для генерации: - "))
lenght = int(input("Длина одного пароля: - "))
incl = input("Включать ли цифры 0123456789? [да/нет] :")
Alpha = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? [да/нет] :")
alpha = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? [да/нет] :")
symbol = input("Включать ли символы !#$%&*+-=?@^_? [да/нет] :")
errsymbol = input("Исключать ли неоднозначные символы il1Lo0O?: [да/нет] :")

while count != 0:

    while len(chars) != lenght:
        if incl == "да":
            chars += random.choice(digits)
            if len(chars) == lenght:
                print(chars)
                break
        if Alpha == "да":
            chars += random.choice(uppercase_letters)
            if len(chars) == lenght:
                print(chars)
                break
        if alpha == "да":
            chars += random.choice(lowercase_letters)
            if len(chars) == lenght:
                print(chars)
                break
        if symbol == "да":
            chars += random.choice(punctuation)
            if len(chars) == lenght:
                print(chars)
                break
        if errsymbol == "нет":
            chars += random.choice(punc2)
            if len(chars) == lenght:
                print(chars)
                break
        if len(chars) < lenght:
            continue
    chars = ""
    count -= 1
    if count != 0:
        continue

print(chars)
