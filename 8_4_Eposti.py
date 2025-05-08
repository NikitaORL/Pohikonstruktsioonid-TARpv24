from tkinter import *
import smtplib, ssl
from email.message import EmailMessage
from tkinter import filedialog

def tuhista(event):
    sisestus.delete(0, END)
    
def saada():
    kelle = sisestus.get().strip()
    kiri = sisestus4.get("1.0", END).strip()
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "nikita.orlenko234@gmail.com"
    password = "tbgx pddd ezym kdsu"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg["Subject"] = sisestus2.get().strip()
    msg["From"] = sender_email
    msg["To"] = kelle
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
        pealkiri2.config(text="Saadetud!")
    except Exception as e:
        pealkiri2.config(text=f"Viga: {e}")
    finally:
        server.quit()


def pilt():
    global file
    file= filedialog.askopenfilename()
    l_lisatud.configure(text=file)
    return file

def vaheta_teema():
    if aken['bg'] == 'white':
        aken.configure(bg="black")
        pealkiri.configure(bg="black", fg="white")
        pealkiri2.configure(bg="black", fg="white")
        pealkiri3.configure(bg="black", fg="white")
        pealkiri4.configure(bg="black", fg="white")
        sisestus.configure(bg="gray", fg="white")
        sisestus2.configure(bg="gray", fg="white")
        sisestus4.configure(bg="gray", fg="white")
        nupp.configure(bg="gray", fg="black")
        nupp_2.configure(bg="gray", fg="black")
    else:
        aken.configure(bg="white")
        pealkiri.configure(bg="lightblue", fg="black")
        pealkiri2.configure(bg="lightblue", fg="black")
        pealkiri3.configure(bg="lightblue", fg="black")
        pealkiri4.configure(bg="lightblue", fg="black")
        sisestus.configure(bg="lightblue", fg="black")
        sisestus2.configure(bg="lightblue", fg="black")
        sisestus4.configure(bg="lightblue", fg="black")
        nupp.configure(bg="gray", fg="black")
        nupp_2.configure(bg="gray", fg="black")

aken = Tk()                      
aken.title("E-kirja saatmine")       
aken.geometry("550x550")        
aken.configure(bg="white")      
aken.resizable(width=True, height=True) 

#------------------------------------------------------------------------------------------------------
# тут заголовки
pealkiri = Label(aken, text="EMAIL:", bg="lightblue", font=("Times New Roman", 25), fg="black", width=10)   
pealkiri2 = Label(aken, text="TEEMA:", bg="lightblue", font=("Times New Roman", 25), fg="black", width=10)
pealkiri3 = Label(aken, text="LISA:", bg="lightblue", font=("Times New Roman", 25), fg="black", width=10)
pealkiri4 = Label(aken, text="KIRI:", bg="lightblue", font=("Times New Roman", 25), fg="black", width=10)
l_lisatud = Label(aken, text="", bg="white", fg="black", font=("Arial", 10))
l_lisatud.place(x=200, y=130)
# тут поля для ввода 
sisestus=Entry(aken, bg="lightblue", font=("Arial", 15), fg="black", width=30)    
sisestus.insert(0, "Näiteks: daniel123@gmail.com")
sisestus.bind("<Button-1>", tuhista)
#---
sisestus2=Entry(aken, bg="lightblue", font=("Arial", 15), fg="black", width=30)  
sisestus.insert(0, "")
#---
sisestus4=Text(aken, bg="lightblue", font=("Arial", 15), fg="black", width=30,)  
sisestus.insert(0, "")

#Кнопка
nupp = Button(aken, text="LISA PILT", bg="gray", font=("Times New Roman", 20), fg="black", relief=RAISED, command=pilt)
nupp_2 = Button(aken, text="SAADA", bg="gray", font=("Times New Roman", 20), fg="black", relief=RAISED, command=saada)
nupp_teema = Button(aken, text="Theme", bg="black", font=("Times New Roman", 20), fg="white", relief=RAISED, command=vaheta_teema)

#-----------------------------------------------------------------------------------------------------
# Это короче чтобы заголовки и кнопочки там работали
pealkiri.place(x=0, y=0)
pealkiri2.place(x=0, y=43)
pealkiri3.place(x=0, y=120)
pealkiri4.place(x=0, y=275)
l_lisatud.place(x=200, y=130)

sisestus.place(x=200, y=0)
sisestus2.place(x=200, y=45)
sisestus4.place(x=200, y=200, height=230)

nupp.place(x=230, y=430)
nupp_2.place(x=405, y=430)
nupp_teema.place(x=10, y=490)
#-----------------------------------------------------------------------------------------------------
# Это короче запуск
aken.mainloop()

