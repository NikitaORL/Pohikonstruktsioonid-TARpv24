
from tkinter import *
k = 0 # Глобальная переменная для счётчика нажатий
def vajutatud():
    global k
    k+=1
    pealkiri.config(text=f"Sa vajasid nuppu {k} korda!")
    nupp.config(text="Vajuta uuesti!", bg="orange",
    fg = "blue")

def vajatudPK(event):
    global k
    k-=1
    pealkiri.config(text=f"Sa vajasid nuppu {k} korda!")
    nupp.config(text="Vajuta uuesti!", bg="orange",
    fg = "blue")

def tuhista(event):
    sisestus.delete(0, END)  # Удаление текста из поля ввода

#---------------------------------------------------------------------------------------------------
aken = Tk()                      # Создание окна
aken.title("Teema 8")           # Заголовок окна
aken.geometry("400x400")        # Размер окна 400x400 пикселей
aken.configure(bg="lightblue")      # Цвет фона — зелёный
aken.resizable(width=False, height=False)  # Запрет изменения размера
aken.iconbitmap("Teema8/meme.ico")     # Иконка окна (должна быть в той же папке)
pealkiri=Label(aken, text="Teema 8", bg="lightblue", font=("Arial", 16), fg="green")  # Заголовок добавление
nupp=Button(aken, text="Vajuta mind!", bg="black", font=("Arial", 12), fg="green", relief=RAISED, command=vajutatud)   # Кнопка добавление
#SUNKEN, RAISED , GROOVE, RIDGE, FLAT - режим кнопки
nupp.bind("<Button-3>", vajatudPK)
sisestus=Entry(aken, bg="white", font=("Arial", 12), fg="black")  # Поле ввода добавление
sisestus.insert(0, "Sisesta midagi")  # Ввод текста по умолчанию
sisestus.bind("<Button-1>", tuhista)  # Удаление текста при нажатии на поле ввода
#--------------------------------------------------------------------------------------------------
# Размещение
pealkiri.pack(pady=20)
nupp.pack()
sisestus.pack(pady=20)

# Запуск
aken.mainloop()