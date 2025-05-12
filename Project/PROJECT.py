from tkinter import *
from PIL import Image, ImageTk  
import smtplib, ssl
from email.message import EmailMessage
from tkinter import messagebox
import json

def game():
    game = Tk()                      
    game.title("GAME")       
    game.geometry("700x550")        
    game.resizable(width=True, height=True)
    game.mainloop()

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


LogiSisse = Tk()                      
LogiSisse.title("Sign in")       
LogiSisse.geometry("700x550")        
LogiSisse.resizable(width=True, height=True)


#----------------------------------
image = Image.open("kazino-s.jpg") 
image = image.resize((700, 550))  
photo = ImageTk.PhotoImage(image)

canvas = Canvas(LogiSisse, width=700, height=550)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, anchor=NW, image=photo)
#------------------------------------------------------------------------------------------------------
# тут заголовки и тд
LogiSissee = Label(LogiSisse, text="Palun logige sisse!",  font=("Times New Roman", 25), fg="black", width=20)
OrlenkoCasino = Label(LogiSisse, text="OrlenkoCasino",  font=("Times New Roman", 25), fg="black", width=20)
#--
sisestus=Entry(LogiSisse, bg="lightblue", font=("Arial", 15), fg="black", width=33)    
sisestus.insert(0, "Näiteks: Uuser123")
sisestus.bind("<Button-1>", tuhista)


LogIn = Button(LogiSisse, text="LogIn", bg="gray", font=("Times New Roman", 20), fg="black", relief=RAISED, command = LogInn)
SignInButton = Button(LogiSisse, text="SignIn", bg="gray", font=("Times New Roman", 20), fg="black", relief=RAISED, command = SignInn)

#-----------------------------------------------------------------------------------------------------
# Это короче чтобы заголовки и кнопочки там работали
LogiSissee.place(x=350, y=150, anchor="center")
OrlenkoCasino.place(x=350, y=50, anchor="center")
#--
sisestus.place(x=168, y=200)
#---
LogIn.place(x=220, y=250)
SignInButton.place(x=370, y=250)
#-----------------------------------------------------------------------------------------------------
# Это короче запуск
LogiSisse.mainloop()