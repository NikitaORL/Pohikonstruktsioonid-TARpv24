import smtplib, ssl
from email.message import EmailMessage
from tkinter import filedialog
from os import system
import random

usernames = []
passwords = []
gmails = []

#---------------------------------------------------------------------------------------
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
        print("Некорректный ввод, попробуйте снова")
        return

    username = input("Введите логин для регистрации: ")
    gmail_reg = str(input("Введите почту для регистрации: "))
    teema_reg = f"Здравствуйте {username}, спасибо за регистрацию на нашем сайте, доп. информацию вы можете найти на сайте: nikitos.com "
    
    if username in usernames:
        print("Этот логин уже занят")
        return  

    usernames.append(username)
    passwords.append(password)
    gmails.append(gmail_reg) 
    print(f"Пользователь {username} успешно зарегистрирован!")
    
    # Отправка письма
    saada_kiri(gmail_reg, teema_reg)  # вызов функции для отправки письма
    system('cls')
    return gmail_reg, teema_reg

#---------------------------------------------------------------------------------------
def change_password():
    username = input("Введите логин для смены пароля: ")
    if username in usernames:
        answer = input("Вы помните свой старый пароль? Да/Нет: ").lower()
        if answer == "Нет" or answer == "нет":
            recover_password()
            
        elif answer == "Да" or answer == "да":  
            old_password = input("Введите старый пароль: ")
            if passwords[usernames.index(username)] == old_password:
                new_password = input("Введите новый пароль: ")
                passwords[usernames.index(username)] = new_password
                print("Пароль успешно изменен")
            else:
                print("Неверный старый пароль")
        else:
            print("Неверный ответ")
    else:
        print("Пользователь не найден")
        system('cls')

#---------------------------------------------------------------------------------------
def recover_password():
    username = input("Введите логин для восстановления пароля: ")
    if username in usernames:
        gmail_reg = str(input("Введите почту для восстановления пароля: "))
        teema_rec = f"Здравствуйте {username}, для восстановления пароля, просим перейти по ссылке: nikitosHelp.com"
        # Передаем два аргумента: gmail_reg и teema_rec
        saada_kiri(gmail_reg, teema_rec)  # Печатаем письмо на почту пользователя
    else:
        print("Пользователь не найден")
        system('cls')

#---------------------------------------------------------------------------------------
def login():
    username = input("Введите логин: ")
    if username in usernames:
        password = input("Введите пароль: ")
        if passwords[usernames.index(username)] == password:
            print(f"Добро пожаловать, {username}!")
        else:
            print("Неверный пароль")
    else:
        print("Пользователь не найден")

#---------------------------------------------------------------------------------------
def saada_kiri(gmail_reg, teema_reg):
    kellele = gmail_reg  # Почта получателя
    teema = teema_reg    # Тема письма

    # HTML контент
    sisu = f'''<!DOCTYPE html>
<head>
</head>
<body>
    <h1>Sending an HTML email from nikitos.com</h1>
    <p>Hello there,</p>
    <a href="https://www.nikitos.ee/">{teema}</a>
</body>
</html>'''

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "nikita.orlenko234@gmail.com"  # От кого письмо
    salasõna = "qhmb kvpm riiv esdp"  # Замените на свой пароль для приложения

    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = kellelt
    msg['To'] = kellele

    msg.set_content(sisu, subtype='html')

    # Отправка письма без файла для отладки
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())  # Шифрованное соединение
            server.login(kellelt, salasõna)  # Вход в аккаунт
            server.send_message(msg)  # Отправка сообщения
            print("Kiri saadetud edukalt!")  # Уведомление о успешной отправке
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")  # Вывод ошибки при неудаче