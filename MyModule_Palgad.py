p = []
i = []

def Lisa(p: list, i: list):
    while True:
        try:
            nimi = input("Введите имя: ")
            if nimi.isalpha():  
                try:
                    palk = float(input("Palk: "))  
                    p.append(palk)
                    i.append(nimi)
                    print("Andmed on lisatud!")
                    print("\n")
                    break  
                except ValueError:
                    print("Palk peab olema arv!")  
            else:
                print("Введите только буквы в имени!")  
        except: 
            print("Введите только буквы!")

def kustumine(p: list, i: list):
    if not p:
        print("Список пуст!")
        return
    while True:
        try:
            nimi = input("Введите имя для удаления: ")
            if nimi in i:
                index = i.index(nimi)  
                print(f"Удалено: {nimi}, зарплата: {p[index]}")
                i.pop(index)  
                p.pop(index)  
                print("\n")
                break
            else:
                print("Имя не найдено!")
        except ValueError:
            print("Введите только буквы!")



def Suurim(p: list, i: list):
    if not p:
        print("Список пуст!")
        return
    max_salary = max(p)
    index = p.index(max_salary)
    print(f"Самая большая зарплата: {max_salary}, имя: {i[index]}")
    print("\n")

def väiksem(p: list, i: list):
    if not p:
        print("Список пуст!")
        return
    min_salary = min(p)
    index = p.index(min_salary)
    print(f"Самая маленькая зарплата: {min_salary}, имя: {i[index]}")
    print("\n")



def Võrsed_palgad(p: list, i: list):
    hulk = set(p)  
    print(hulk)
    
    for palk in hulk: 
        k = p.count(palk)  
        
        if k > 1:  
            print(f"Palk {palk}")  
            for j in range(len(p)):  
                if p[j] == palk:  
                    print(f"Saab kätte {i[j]}")
                    print("\n")

def otsi(p: list, i: list):
    if not i:  
        print("Список пуст!")
        return
    while True:
        try:
            nimi = input("Введите имя для поиска: ").lower()
            if nimi in i:  
                index = i.index(nimi)  
                print(f"Имя: {nimi}, зарплата: {p[index]}")
                print("\n")
                break  
            else:
                print("Имя не найдено!")  
        except ValueError:
            print("Введите только буквы!")  


def Top(p: list, i: list):
    while True:
        print("\n")
        print("Хотите увидеть бедных или богатых?")
        try:
            choice2 = input("R - богатые, V - бедные:  ")
            if choice2 == "R":
                top = int(input("Хорошо! Сколько богатых вы хотите увидеть?: "))
                top = min(top, len(p))
                print(f"{top} самых богатых:")

                for j in sorted(zip(p, i), reverse=True)[:top]:
                    print(j[1])  # j[1] - это имя человека, получающее зарплату
            elif choice2 == "V":
                top2 = int(input("Хорошо! Сколько бедных вы хотите увидеть?: "))
                top2 = min(top2, len(p))
                print(f"{top2} самых бедных:")

                for j in sorted(zip(p, i))[:top2]:
                    print(j[1])  
            else:
                print("Неверный выбор. Пожалуйста, выберите 'R' или 'V'.")
                continue

            # Запрос на продолжение
            continue_choice = input("\nХотите продолжить? (Y - Да, N - Нет): ").strip().upper()
            if continue_choice == 'N':
                break  # Выход из цикла и возврат в меню
            elif continue_choice != 'Y':
                print("Неверный выбор. Пожалуйста, выберите 'Y' или 'N'.")
                continue
        except ValueError:
            print("Введите только числа, предложенные выше!")
            continue

