import MyModule777


usernames = []
passwords = []


while True:
        print("Добро пожаловать в программу!")
        print("Пожалуйста войдите или зарегистрируйтесь")
        print("1 - войти")
        print("2 - зарегистрироваться")
        print("3. Смена пароля")
        print("4. Восстановление пароля")
        print("5. Выход")

        try:
            choice = int(input("Выберите пункт: "))
        except ValueError:
            print("Ошибка! Введите число")
            continue
        
        if choice == 1:
            MyModule777.login()
        elif choice == 2:
            MyModule777.register()
        elif choice == 3:
            MyModule777.change_password()
        elif choice == 4:
            MyModule777.recover_password()
        elif choice == 5:
            print("До свидания!")
            break  
        else:
            print("Неверный выбор, попробуйте снова")

