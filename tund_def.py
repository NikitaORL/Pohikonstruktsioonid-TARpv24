# from tund_def import * 
# # 1) artimetic funktsiooni kasutamine
# a = float(input("Sisesta arv 1: "))
# b = float(input("Sisesta arv 2: "))
# c = input("Sisesta operatsioon: ")
# v=arithmetic(a, b, c)
# print(v)

#------------------------------------------

# # 2) is_year_leap funktsiooni kasutamine
# aasta = int(input("Sisesta aasta"))
# v=is_year_leap(aasta)
# if v == True:
#     print(f"{aasta} on liigaasta")
# else:
#     print(f"{aasta} ei ole liigaasta")

#------------------------------------------

# # 3) square funktsiooni kasutamine
# S,P,d=square(float(input("sisesta külg")))
# print(S,P,d)

#------------------------------------------

# 4) 
# def seasonInput()->str:
#     k=int(input("Siseta kuu number:  "))
# while True:
#     if k in range(1, 13):
#         break
#     else:
#         k=int(input("Palun siseta kuu number:  "))
# return season(k)

#------------------------------------------

# 5) Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых
#  (каждый год размер его вклада увеличивается на 10%. 
#  Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

# def bank(eur: float, years: int) -> float:
#     for i in range(years):
#         eur = eur * 1.10  
#     return round(eur, 2)  # Переносим return за цикл, чтобы учитывать все годы


# a = float(input("Siseta oma summa: "))  
# b = int(input("Siseta aastate arv: "))  

# v = bank(a, b)  
# print(v) 

#-------------------------------------------------------------------------------------------

# 6) Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, 
# если оно простое, и False - иначе.

# def is_prime(number: int) -> bool:
#     if number <= 1:
#         return False  # Числа меньше или равные 1 не являются простыми
#     for i in range(2, int(number ** 0.5) + 1):  # Проверка делителей до корня из числа
#         if number % i == 0:  # Если число делится на i, оно не простое
#             return False
#     return True  # Если не нашли делителей, значит число простое

# number = int(input("Введите число для проверки на простоту: "))
# print(is_prime(number))

#-----------------------------------------------------------------------------------------------

# 7) Написать функцию date, принимающую 3 аргумента — день, месяц и год.
#  Вернуть True, если такая дата есть в нашем календаре, и False иначе.

import datetime

def date(päev: int, kuu: int, aasta: int) -> bool:
    try:
        datetime.datetime(aasta, kuu, päev)
        return True  # Если ошибка не возникла, значит дата корректна
    except ValueError:
        return False  # Если возникла ошибка, дата некорректна

v=input("Пожадуйста введите дату: ")
print(v)

 