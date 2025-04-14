sõne_list = []

while True:
    print("\nВыберите действие с списком:")
    print("1. Добавить элемент в конец списка (append)")
    print("2. Расширить список (extend)")
    print("3. Вставить элемент в список (insert)")
    print("4. Удалить элемент по значению (remove)")
    print("5. Удалить элемент по индексу (pop)")
    print("6. Найти индекс элемента (index)")
    print("7. Посчитать количество элементов (count)")
    print("8. Отсортировать список (sort)")
    print("9. Развернуть список (reverse)")
    print("10. Скопировать список (copy)")
    print("11. Очистить список (clear)")
    print("12. Проверить наличие элемента в списке (in)")
    print("13. Получить длину списка (len)")
    print("14. Перевести все строки в верхний регистр")
    print("15. Перевести все строки в нижний регистр")
    print("16. Удалить дубликаты из списка")
    print("17. Объединить список в строку")
    print("18. Разделить строку в список")
    print("19. Сравнить два списка")
    print("20. Заменить элемент по индексу")
    print("21. Перевернуть список через срез")

    choice = input("Введите номер: ")

    if choice == '1':
        while True:
            try:
                t = input("Введите элемент для добавления в список: ")
                if t.isalpha():
                    sõne_list.append(t)
                    break
                else:
                    print("Ошибка! Введите только текст.")
            except Exception as e:
                print(f"Ошибка: {e}. Попробуйте снова.")
        print("Список после добавления:", sõne_list)

    elif choice == '2':
        try:
            ext_list = input("Введите список, чтобы добавить через запятую: ").split(',')
            ext_list = [item.strip() for item in ext_list]
            sõne_list.extend(ext_list)
        except Exception as e:
            print(f"Ошибка: {e}. Попробуйте снова.")
        print("Список после расширения:", sõne_list)

    elif choice == '3':
        try:
            t = input("Введите элемент для вставки: ")
            indx = int(input("Введите индекс для вставки: "))
            if 0 <= indx <= len(sõne_list):
                sõne_list.insert(indx, t)
            else:
                print("Ошибка! Индекс вне допустимого диапазона.")
        except ValueError:
            print("Ошибка! Введите правильный индекс.")
        print("Список после вставки:", sõne_list)

    elif choice == '4':
        try:
            t = input("Введите элемент для удаления: ")
            if t in sõne_list:
                sõne_list.remove(t)
            else:
                print("Ошибка! Элемент не найден.")
        except Exception as e:
            print(f"Ошибка: {e}. Попробуйте снова.")
        print("Список после удаления элемента:", sõne_list)

    elif choice == '5':
        try:
            indx = int(input("Введите индекс элемента для удаления: "))
            if 0 <= indx < len(sõne_list):
                removed_item = sõne_list.pop(indx)
                print(f"Удалён элемент: {removed_item}")
            else:
                print("Ошибка! Индекс вне допустимого диапазона.")
        except ValueError:
            print("Ошибка! Введите правильный индекс.")
        print("Список после удаления элемента:", sõne_list)

    elif choice == '6':
        t = input("Введите элемент для поиска индекса: ")
        if t in sõne_list:
            index = sõne_list.index(t)
            print(f"Индекс элемента '{t}': {index}")
        else:
            print("Ошибка! Элемент не найден.")

    elif choice == '7':
        t = input("Введите элемент для подсчёта: ")
        count = sõne_list.count(t)
        print(f"Количество элемента '{t}': {count}")

    elif choice == '8':
        sort_order = input("(введите 'y' для сортировки по возрастанию или 'n' для убывания): ").lower()
        if sort_order == 'y':
            sõne_list.sort()
            print("Список отсортирован по возрастанию.")
        elif sort_order == 'n':
            sõne_list.sort(reverse=True)
            print("Список отсортирован по убыванию.")
        else:
            print("Ошибка! Введите 'y' или 'n'.")
        print("Список после сортировки:", sõne_list)

    elif choice == '9':
        sõne_list.reverse()
        print("Список после разворота:", sõne_list)

    elif choice == '10':
        copy_list = sõne_list.copy()
        print("Копия списка:", copy_list)

    elif choice == '11':
        sõne_list.clear()
        print("Список очищен.")

    elif choice == '12':
        elem = input("Введите элемент для проверки: ")
        if elem in sõne_list:
            print("Элемент найден в списке.")
        else:
            print("Элемент не найден.")

    elif choice == '13':
        print(f"Длина списка: {len(sõne_list)}")

    elif choice == '14':
        sõne_list = [item.upper() if isinstance(item, str) else item for item in sõne_list]
        print("Все элементы переведены в верхний регистр:", sõne_list)

    elif choice == '15':
        sõne_list = [item.lower() if isinstance(item, str) else item for item in sõne_list]
        print("Все элементы переведены в нижний регистр:", sõne_list)

    elif choice == '16':
        sõne_list = list(dict.fromkeys(sõne_list))
        print("Список после удаления дубликатов:", sõne_list)

    elif choice == '17':
        joined = ', '.join(map(str, sõne_list))
        print("Объединённая строка:", joined)

    elif choice == '18':
        line = input("Введите строку, которую нужно разделить по запятой: ")
        sõne_list = [item.strip() for item in line.split(',')]
        print("Список после разделения строки:", sõne_list)

    elif choice == '19':
        other_list = input("Введите другой список (через запятую): ").split(',')
        other_list = [item.strip() for item in other_list]
        if sõne_list == other_list:
            print("Списки одинаковы.")
        else:
            print("Списки разные.")

    elif choice == '20':
        try:
            indx = int(input("Введите индекс для замены: "))
            new_val = input("Введите новое значение: ")
            if 0 <= indx < len(sõne_list):
                sõne_list[indx] = new_val
                print("Элемент заменён.")
            else:
                print("Ошибка! Индекс вне допустимого диапазона.")
        except ValueError:
            print("Ошибка! Введите корректный индекс.")

    elif choice == '21':
        sõne_list = sõne_list[::-1]
        print("Список перевёрнут срезом:", sõne_list)

    else:
        print("Неверный выбор! Попробуйте снова.")
