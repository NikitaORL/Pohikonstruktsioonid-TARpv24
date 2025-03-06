3 2 Известны оценки по физике каждого ученика двух классов. Определить среднюю оценку в каждом классе.
Количество учащихся в каждом классе одинаковое.

import random
arv1 = 0 
arv2 = 0 

num_õpilased = random.randint(10, 35) # Колличесто учеников от 5 до 35 человек
for i in range(num_õpilased):
    while True:
        try:
            a = random.randint(1, 5)  # Генерирую случайное число для оценки
            if a > 0:
                arv1 += a  # Суммирую оценки для первого класса
                break
        except ValueError:
            print("Что то пошло не так")

for i in range(num_õpilased):
    while True:
        try:
            a = random.randint(1, 5)  # Генерирую второе случайно число для оценки (скопировал первый кусок кода)
            if a > 0:
                arv2 += a  # Суммирую оценки для первого класса
                break
        except ValueError:
            print("Что то пошло не так")




keskmine_esimine = arv1 / num_õpilased
keskmine_teine = arv2 / num_õpilased


print(f"Количество учеников в каждом классе: {num_õpilased}")
print(f"Средняя оценка 1-го класса: {keskmine_esimine}")
print(f"Средняя оценка 2-го класса: {keskmine_teine}")
--------------------------------------------------------------------------------------------------------------
4 В области 12 районов. Известны количество жителей (в тысячах человек) и площадь (в км2) каждого района. 
Определить среднюю плотность населения по области в целом. Исходные данные рандомные.


import random
naabruskond=12
elanikud=0
ruutKm2=0

for i in range(naabruskond):
        try:
            ruutKm2=random.randint(10, 45) #Площадь районов от 10 до 45км2
            elanikud=random.randint(100, 10000) #Колличество жителей от 100 до 10к
            Vastus=elanikud/ruutKm2
            print(f"Для района {i+1}: Площадь = {ruutKm2} км², Количество жителей = {elanikud}, Плотность населения = {Vastus} человек/км²")
        except:
            print("Ошибка при выполнении команды")

----------------------------------------------------------------------------------------------------------------------------
Известны средние оценки каждого из  учеников класса. 
Определить минимальную и максимальную оценки. 
(Оценки и количество учеников получаем случайным образом). 
Использовать только цикл и сравнительные операторы. max() и min() не использвать.

import random

num_õpilased = random.randint(10, 35)
min_hinne = 6  
max_hinne = 0  

for i in range(num_õpilased):
    hinne = random.randint(1, 5)  
    print(f"Оценка ученика {i+1}: {hinne}")

    if hinne > max_hinne:
        max_hinne = hinne
    if hinne < min_hinne:
        min_hinne = hinne

print(f"Минимальная оценка: {min_hinne}")
print(f"Максимальная оценка: {max_hinne}")
------------------------------------------------------------------------------------------

number = int(input("kui palju maju teha?"))

for kogus in range(0, number):
    print("   ~~~~~")
    print("  /_____\\")
    print("  | []  |")
    print("  -------")
    print()

