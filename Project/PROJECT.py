from tkinter import *
from PIL import Image, ImageTk  
from tkinter import messagebox
import random

def game():
    game = Toplevel(LogiSisse)
    game.title("GAME")       
    game.geometry("700x550")        
    game.resizable(width=True, height=True)

    try:
        image2 = Image.open("clash3.png")
        image2 = image2.resize((700, 550))
        photo2 = ImageTk.PhotoImage(image2)

        canvas2 = Canvas(game, width=700, height=550)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, anchor=NW, image=photo2)
        canvas2.image = photo2
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить фон:\n{str(e)}")
        return

    player_cards = []
    dealer_cards = []
    stake_var = StringVar()
    balance = 100
    balance_var = StringVar(value=f"Баланс: {balance} €")

    def get_score(cards):
        score = sum(cards)
        if 11 in cards and score > 21:
            cards[cards.index(11)] = 1
            score = sum(cards)
        return score

    def draw_card():
        return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11])

    def update_status():
        player_score = get_score(player_cards)
        cards_label.config(text=f"Ваши карты: {player_cards} | Очки: {player_score}")

    def update_balance_display():
        balance_var.set(f"Баланс: {balance} €")

    def start_game():
        nonlocal balance
        try:
            stake = int(stake_var.get())
        except ValueError:
            messagebox.showwarning("Ошибка", "Введите числовую ставку")
            return

        if stake <= 0:
            messagebox.showwarning("Ошибка", "Ставка должна быть больше 0")
            return
        if stake > balance:
            messagebox.showwarning("Ошибка", "Недостаточно средств для ставки")
            return

        balance -= stake
        update_balance_display()

        player_cards.clear()
        dealer_cards.clear()
        player_cards.append(draw_card())
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())
        update_status()
        result_label.config(text="")

    def hit():
        player_cards.append(draw_card())
        update_status()
        if get_score(player_cards) > 21:
            result_label.config(text="Вы проиграли!", fg="red")

    def stand():
        nonlocal balance
        while get_score(dealer_cards) < 17:
            dealer_cards.append(draw_card())

        p = get_score(player_cards)
        d = get_score(dealer_cards)
        try:
            stake = int(stake_var.get())
        except ValueError:
            stake = 0

        if d > 21 or p > d:
            win = stake * 2
            balance += win
            result_label.config(text=f"Вы выиграли! +{win} €", fg="green")
        elif p == d:
            balance += stake
            result_label.config(text="Ничья (ставка возвращена)", fg="blue")
        else:
            result_label.config(text="Вы проиграли!", fg="red")
        update_balance_display()

    # Интерфейсные элементы (на фоне)
    stake_label = Label(game, text="Ставка:", bg="white", font=("Arial", 25))
    stake_entry = Entry(game, textvariable=stake_var, font=("Arial", 25), width=10)
    balance_label = Label(game, textvariable=balance_var, bg="white", font=("Arial", 12))
    play_button = Button(game, text="Играть", font=("Arial", 14), command=start_game)
    hit_button = Button(game, text="Ещё", font=("Arial", 14), command=hit)
    stand_button = Button(game, text="Хватит", font=("Arial", 14), command=stand)
    result_label = Label(game, font=("Arial", 14), bg="white")

    # Расположение элементов
    stake_label.place(x=100, y=105)
    stake_entry.place(x=250, y=105)
    balance_label.place(x=592, y=0)
    play_button.place(x=50, y=150)
    hit_button.place(x=150, y=150)
    stand_button.place(x=250, y=150)
    result_label.place(x=50, y=200)

# ----------------------------- Вход и регистрация -----------------------------

def tuhista(event):
    sisestus.delete(0, END)

def SignInn():
    username = sisestus.get().strip()
    if not username:
        messagebox.showwarning("Пусто", "Введите имя пользователя")
        return

    try:
        with open("Project//usernames2.txt", "r", encoding="utf-8") as f:
            users = [line.strip().replace("username:", "") for line in f]
        if username in users:
            messagebox.showinfo("Есть", "Такой пользователь уже есть")
            return

        with open("Project//usernames2.txt", "a", encoding="utf-8") as f:
            f.write(f"username:{username}\n")

        messagebox.showinfo("Ок", "Регистрация прошла успешно")
        game()
    except:
        messagebox.showerror("Ошибка", "Не удалось сохранить пользователя")

def LogInn():
    nimi = sisestus.get().strip()
    if not nimi:
        messagebox.showwarning("Пусто", "Введите имя пользователя")
        return

    try:
        with open("Project//usernames2.txt", "r", encoding="utf-8") as f:
            users = [line.strip().replace("username:", "") for line in f]
        if nimi in users:
            messagebox.showinfo("Добро пожаловать", f"{nimi} вошёл")
            game()
        else:
            messagebox.showerror("Ошибка", "Такой пользователь не найден")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл пользователей не найден")

# ----------------------------- Главное окно -----------------------------

LogiSisse = Tk()                      
LogiSisse.title("Sign in")       
LogiSisse.geometry("700x550")        
LogiSisse.resizable(width=True, height=True)

image = Image.open("kazino-s.jpg") 
image = image.resize((700, 550))  
photo = ImageTk.PhotoImage(image)

canvas = Canvas(LogiSisse, width=700, height=550)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=NW, image=photo)

LogiSissee = Label(LogiSisse, text="Palun logige sisse!",  font=("Times New Roman", 25), fg="black", width=20)
OrlenkoCasino = Label(LogiSisse, text="OrlenkoCasino",  font=("Times New Roman", 25), fg="black", width=20)

sisestus = Entry(LogiSisse, bg="lightblue", font=("Arial", 15), fg="black", width=33)    
sisestus.insert(0, "Näiteks: Uuser123")
sisestus.bind("<Button-1>", tuhista)

LogIn = Button(LogiSisse, text="LogIn", bg="gray", font=("Times New Roman", 20), fg="black", command=LogInn)
SignInButton = Button(LogiSisse, text="SignIn", bg="gray", font=("Times New Roman", 20), fg="black", command=SignInn)

LogiSissee.place(x=350, y=150, anchor="center")
OrlenkoCasino.place(x=350, y=50, anchor="center")
sisestus.place(x=168, y=200)
LogIn.place(x=220, y=250)
SignInButton.place(x=370, y=250)

LogiSisse.mainloop()