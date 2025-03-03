
# print("Tere! Olen sinu uus sõber - Python!")
# nimi=input("Siseta oma nimi:")
# print(f"{nimi} oi kui ilus nimi!")
# while 1:
#     try:
#         soov=int(input(f"{nimi} Kas leian sinu keha indeksi? 0-ei, 1-jah => "))
#         if soov==1:
#             print("Indeksi leidmine...")
#             try:
#                 pikkus=int(input("Mis on sinu pikkus?"))
#                 try:
#                     mass=float(input("Mis on sinu kaal?"))
#                     indeks=mass/(0.1*pikkus)**2
#                     print(f"{nimi}, sinu keha indeks on: {indeks}")
#                     if indeks < 16:
#                         print("Tervisele ohtlik alakaal")
#                     elif indeks==16-19:
#                         print("Alakaal")
#                     elif indeks==19 - 25:
#                         print("Normaalkaal")
#                     elif indeks==25 - 30:
#                         print("Ülekaal")
#                     elif indeks==30 - 35:
#                         print("Rasvumine")
#                     elif indeks==35 - 40:
#                         print("Tugev rasvumine")
#                     elif indeks>40:
#                         print("Tervisele ohtlik rasvumine")
#                         break
#                 except:
#                     print("Vale kaalu formaat!")
#             except:
#                 print("Vale pikkuse formaat!")
#         elif soov==0:
#             print("Kahju! See on väga kasulik info!")
#             break
#         else:
#             print("Vale valik. Saab valida ainult 1 või 0")
#     except:
#         print("Vale soov!")

#10 практических заданий по теме Циклы
# -----------------------------------------------------------------------------------------------------------
# 1.    Вводят 15 чисел. Определить, сколько среди них целых.

# täisarvud=0
# for i in range(3):
#     while True:
#         try:
#             arv=float(input(f"Siseta {i+1}. arv"))
#             break
#         except:
#             print("Kirjuta ainult numbrid!")
#         if arv==int(arv): täisarvud+=1
#         print(f"Täisarvude kogus: {täisarvud}")
# -------------------------------------------------------------------------------------
  # 2. Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
# summa = 0
# while True:
#     try:
#         A = int(input("Введите число A: "))
        
#         # Проверяем, что A больше 1
#         if A > 1:
#             for i in range(1, A + 1):  # Числа от 1 до A
#                 summa += i  # Добавляем число в сумму
#             print(f"Summa võrdub {summa}-ga")  # Выводим результат
#             break  # Выход из цикла, если всё правильно
#         else:
#             print("Arv A peab olema rohkem kui 1!")
    
#     except ValueError:
#         print("Vale formaat!")  # Обрабатываем неправильный формат ввода
# ------------------------------------------------------------------------------------------------
# 5. Составьте программу, которая вычисляет сумму только отрицательных из N чисел. Значение N вводится с клавиатуры.
# summa = 0
# while True:
#     try:
#         N = int(input("Siseta N:"))
#         if N > 1:
#             for i in range(1, N + 1):
#                 arv = float(input(f"Siseta {i}. arv"))
#                 if arv<0:
#                     summa+=arv
#             print(f"Summa võrdub {summa}-ga")
#             break
#         else:
#             print("Arv A peab olema rohkem kui 1")
#     except ValueError:
#         print("Palun sisesta kehtiv number.")
# ------------------------------------------------------------------------------------------------------
# 15. Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# ...................
# 0 1 2 3 4 5 6 7 8 9
# for j in range(10):
#     for i in range(10):
#         print(i,end=" ")
#     print()
# print()
# ----------------------------------------------------------------------------------------------------------------
#Вводят 8 чисел. Найти их произведение (только положительных)
# number_arv=0
# for i in range(0, 8):
#     while True:
#         try:
#             a = int(input("Введите число:"))
#             break
#         except:
#             print("АШИБКА!")
#         if a>0:
#             number_arv += a
#             print(f"Сумма: {number_arv} ")
# --------------------------------------------------------------------------------------------------------------
# 4. Составьте программу, выводящую на экран квадраты чисел от 10 до 20.

# 10. Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.
# for j in range(10):
#     a1=float(input("Певрое число: "))
#     a2=float(input("Второе число: "))
#     if a1>a2:
#         print(f"Suurem on {a1}")
#     elif a2>a1:
#         print(f"Suurem on {a2}")
# print()
# --------------------------------------------------------------------------------------------------------
