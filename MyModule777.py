import math
import string

usernames = []
passwords = []

def login():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if username in usernames and passwords[usernames.index(username)] == password:
        print("Вы успешно вошли!")
    else:
        print("Неверный логин или пароль.")

def register():
    username = input("Введите логин для регистрации: ")
    if username in usernames:
        print("Этот логин уже занят.")
    else:
        password = input("Введите пароль для регистрации: ")
        usernames.append(username)
        passwords.append(password)
        print(f"Пользователь {username} успешно зарегистрирован!")

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

def recover_password():
    username = input("Введите логин для восстановления пароля: ")
    if username in usernames:
        print(f"Ваш пароль: {passwords[usernames.index(username)]}")
    else:
        print("Пользователь не найден.")g