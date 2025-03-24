import math
import string
from os import system
import random


usernames = []
passwords = []

def register():
    gen = input("Хотите ли вы сгенерировать паролт? 1 - да, 2 - нет: ")

    if gen == "1":
        str0 = ".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0 + str1 + str2 + str3
        ls = list(str4)
        random.shuffle(ls)
        password = ''.join([random.choice(ls) for _ in range(12)])
        print(f"Сгенерированный пароль: {password}")
    elif gen == "2":
        password = input("Введите пароль для регистрации: ")
    else:
        print("Некорректный ввод, попробуйте снова.")
        return

    username = input("Введите логин для регистрации: ")  

    if username in usernames:
        print("Этот логин уже занят.")
        return  

    usernames.append(username)
    passwords.append(password)
    print(f"Пользователь {username} успешно зарегистрирован!")
    system('cls')

def change_password():
    username = input("Введите логин для смены пароля: ")
    if username in usernames:
        old_password = input("Введите старый пароль: ")
        if passwords[usernames.index(username)] == old_password:
            new_password = input("Введите новый пароль: ")
            passwords[usernames.index(username)] = new_password
            print("Пароль успешно изменен.")
        else:
            print("Неверный старый пароль.")
    else:
        print("Пользователь не найден.")
        system('cls')

def recover_password():
    username = input("Введите логин для восстановления пароля: ")
    if username in usernames:
        print(f"Ваш пароль: {passwords[usernames.index(username)]}")
    else:
        print("Пользователь не найден.")
        system('cls')