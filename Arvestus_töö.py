import  MyModule_ArvestusTöö 
import random
opilased = []
puudumised = []

def main():
    syllables = ["Ива", "Пет", "Сид", "Куз", "Смир", "Вас", "Поп", "Мих", "Нов", "Фед"]
    endings = ["нов", "ров", "кин", "ский", "чев", "ов", "ев", "ков"]
    return random.choice(syllables) + random.choice(endings)

print("Здраствуйте учитель, добро подаловать в программу!")
print("\n")
print("Сегодня состоится комиссия у учеников, которые имеют 80 и более прогулов")
print("\n")
õpilaste_arv = int(input("Пожалуйста введите колличество учеников: "))
print("\n")

for i in range(õpilaste_arv):
    puuudumised = random.randint(0, 150)
    opilased.append(main())
    puudumised.append(puuudumised)

print("Список учеников и их прогулов:")
for i in range(õpilaste_arv):
    print(f"{opilased[i]} - Прогулы: {puudumised[i]}")

while True:
    print("\n\n\n")
    print("Увидеть топ лучших учеников - 1")
    print("Показать список в порядке возрастания прогулов - 2")
    print("Показать список учеников, отправленных на комиссию - 3")
    print("Отчислить учеников, у которых прогулов больше чем 100 - 4")
    print("Дать взятку учителю, чтобы ученик не был отчислен - 5")
    print("Выход - 6")

    try:
        choice = int(input("Выберите пункт: "))
    except ValueError:
        print("Ошибка! Введите число.")
        continue

    if choice == 1:
        MyModule_ArvestusTöö.top5(opilased, puudumised)
