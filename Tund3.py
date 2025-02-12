# from random import *
# # Näidis 1

# arv=randint(0,10)
# print(arv)
# if arv>5:
#     print("***********")
#     print(f"Arv {arv} suurem kui 5!")
#     print("***********")
# if arv>5: print(f"Arv {arv} suurem kui 5")

# #Näidis 2
# arv=randit(-10,10)
# if arv>0:
#     print("See arv on positiivne")
# else:
#     print("See arv on negatiivne") #viga!

    

# if arv>0:
#         print("See arv on positiivne")
# elif arv==0:
#     print("0")
# else:
#     print("See arv on negatiivne")

# ____________________________________________________________
# Ülesanded: Tingimuslik operaator IF
#1. Juku
nimi=str(input("Palun siseta om animi!"))
if nimi.isupper() and nimi.lower()=="juku":
    print("Lähme kinno")
    try:
        vanus=int(input("Kui vana sa oled?"))
        if vanus<0 or vanus<100:
            pilet="!!!"
        if vanus<=6:
            pilet="Tasuta"
        elif vanus<=14:
            pilet="Laste pilet"
        elif vanus <=65:
            pilet="Täospilet"
        elif vanus<=100:
            pilet="Sooduspilet"
        print(pilet)
    except Exception as e:
        print("Tekkis viga:",e)
else:
    print("Ma hakkan plaanid")
# _______________________________________________________________
# b) Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)
saddh