import random

def top(opilased, puudumised):
    top=int(input("Введите колличество учеников, которых хотите увидеть: "))
    print("\n\n\n")
    if top > len(opilased):
        print("Недостаточно учеников в списке.")
        print("\n\n\n")
        return
    for i in range(top):
        print(f"{opilased[i]} - Прогулы: {puudumised[i]}")
        print("\n\n\n")
#-------------------------------------------------------------------------------------

def sort_students(opilased, puudumised):
    data = list(zip(opilased, puudumised))  # Объединяем списки
    data.sort(key=lambda x: x[1])  # Сортируем по прогулов
    for name, absences in data:  # Выводим результат
        print(f"{opilased} - Прогулы: {puudumised}")
#--------------------------------------------------------------------------------------
def commission(opilased, puudumised):
    for i in range(len(opilased)):  
        if puudumised[i] >= 80:  
            print(f"{opilased[i]} - Прогулы: {puudumised[i]}")

#--------------------------------------------------------------------------------------
def remove_students(opilased, puudumised):
    # Прохожу по всем ученикам
    i = 0
    while i < len(opilased):
        if puudumised[i] > 100:
            print("\n\n")
            print(f"{opilased[i]} - Прогулы: {puudumised[i]}")
            print("Ученик отчислен.")
            opilased.pop(i)
            puudumised.pop(i)
        else:
            i += 1  # Если ученик не отчислен то иду к след
#--------------------------------------------------------------------------------------
def vzatka(opilased, puudumised):
    Vopilane = input("Ввелите фамилию ученика которого хотите спасти:  ")
    if Vopilane in opilased:
        index = opilased.index(Vopilane)
    elif  puudumised[index] >= 80:
        print(f"Ученик {Vopilane} имеет {puudumised[index]} прогулов")
        money=int(input("Введите сумму взятки $ : "))
    elif money >= 500:
        print("Секретарь убрал 50% прогулов")
