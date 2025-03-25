import random

def top5(opilased, puudumised):
    top=int(input("Введите колличество учеников, которых хотите увидеть: "))
    print("\n\n\n")
    if top > len(opilased):
        print("Недостаточно учеников в списке.")
        print("\n\n\n")
        return
    for i in range(top):
        print(f"{opilased[i]} - Прогулы: {puudumised[i]}")
        print("\n\n\n")