Määrake H aasta jooksul pangas kogunenud rahasumma, kui Vlad'i esialgne sissemakse oli Y dollarit ja sissemakse tehti
tingimustel Z%aastas

print("Tere, täna hakkame arvutama kogunenud deposiidi summat!")

while True:
    try:
        Y = float(input("Palun märkige esialgne tagatisraha summa: "))
        H = float(input("Mitu aastat oli tagatisraha? "))
        Z = float(input("Kui suur on hoiuse aastane intress? "))
        
        if Y <= 0 or H <= 0 or Z <= 0:
            print("Kõik väärtused peaksid olema positiivsed. Proovige uuesti!")
            continue
        
        T = Y * (1 + Z / 100) ** H
        print(f"Kogunenud hoiuses olev summa on {H} aasta pärast {T} eurot!")
        
        break
    except ValueError:
        print("Palun sisestage ainult numbrid! Proovige uuesti!")
-----------------------------------------------------------------------------------

print("See on programm ainult positiivsete arvude arvutamiseks")

while True:
    try:
        Num1 = int(input("Palun sisesta esimene number: "))
        Num2 = int(input("Palun sisesta teine number: "))

        summa = 0

        if Num1 > 0:
            summa += Num1
        elif Num2 > 0:
            summa += Num2

        print(f"Positiivsete arvude summa on: {summa}")

        if Num1 == Num2:
            print("Lõpp")
            break  

    except ValueError:
        print("Palun sisesta kehtiv number!")
-----------------------------------------------------------------------------------
import random

Poisii = 0
print("Üks tuba mahutab 3 inimest")
print("Kas poisid ja tüdrukud tuleks paigutada koos või eraldi?")

while True:
    try:
        KasutajaAns = int(input("Koos - 1, eraldi - 2: "))
        
        if KasutajaAns == 1:
            Inimesed = random.randrange(10, 40, 10)
            print(f"Klassis on {Inimesed} inimest")
            TüdProts = random.randrange(10, 80, 10)
            print(f"Tüdrukute osakaal on {TüdProts}% ")
            
            ruumid = Inimesed / 3
            ruumid = int(ruumid) if Inimesed % 3 == 0 else int(ruumid) + 1
            print(f"Sportlaste majutamiseks on vaja broneerida {ruumid} tuba")
            break  
        
        elif KasutajaAns == 2:
            Inimesed = random.randrange(10, 40, 10)
            print(f"Klassis on {Inimesed} inimest")
            TüdProts = random.randrange(10, 80, 10)
            print(f"Tüdrukute osakaal on {TüdProts}% ")

         
            tüdrukud = Inimesed * (TüdProts / 100)
            poisid = Inimesed - tüdrukud
            print(f"Klassis on {poisid} poisid ja {tüdrukud} tüdrukud")

            ruumid_tüdrukud = tüdrukud / 3
            ruumid_poisid = poisid / 3

            ruumid_tüdrukud = int(ruumid_tüdrukud) if tüdrukud % 3 == 0 else int(ruumid_tüdrukud) + 1 #Kasurasin ChatGPT
            ruumid_poisid = int(ruumid_poisid) if poisid % 3 == 0 else int(ruumid_poisid) + 1 #GPT

            print(f"Tüdrukute jaoks on vaja broneerida {ruumid_tüdrukud} tuba.")
            print(f"Poiste jaoks on vaja broneerida {ruumid_poisid} tuba.")
            break  
        
        else:
            print("Palun siseta ainult 1 või 2")
    
    except ValueError:
        print("Sisestasite vale väärtuse. Palun sisestage number 1 või 2.")