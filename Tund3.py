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
# nimi=str(input("Palun siseta om animi!"))
# if nimi.isupper() and nimi.lower()=="juku":
#     print("Lähme kinno")
#     try:
#         vanus=int(input("Kui vana sa oled?"))
#         if vanus<0 or vanus<100:
#             pilet="!!!"
#         if vanus<=6:
#             pilet="Tasuta"
#         elif vanus<=14:
#             pilet="Laste pilet"
#         elif vanus <=65:
#             pilet="Täospilet"
#         elif vanus<=100:
#             pilet="Sooduspilet"
#         print(pilet)
#     except Exception as e:
#         print("Tekkis viga:",e)
# else:
#     print("Ma hakkan plaanid")
# _______________________________________________________________
# b) Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)

# Esimine=float(input("palun öelge mulle seina esimine pikkus "))
# Teine=float(input("Palun öelge mulle seina teine pikkus"))
# P=(Esimine*Teine)
# print("Saabub kokkuvõte...")
# print(f"ruumi pindala on võrdne {P} ")
# vas=str(input("Kas soovite oma põrandat renoveerida?")).lower()
# if vas=="jah":
#     try:
#         Hind=float(input("Milline on ruutmeetri hind?"))
#         kogu_hind=P*Hind
#         print(f"remondi maksumus on {kogu_hind} eurot")
#     except:
#         ("midagi läks valesti!!!")
# else:
#     print("midagi läks valesti!!!")

#4 Allahindus Leia 30% soodustusega hinna, kui alghind on suurem kui 700
# print("Tere maalim!")
# number=int(input("Palun sisestage alghind"))
# if number>700:
#     print("Saabub kokkuvõte...")
#     vastus=number*0.7
#     print(f"Teie summa on võrdne {vastus} eurot")
# else:
#     print("Something went wrong!")

#5 Temperatuur Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
# temp=int(input("Milline on temperatuur praegu"))
# if temp>18 or temp==18:
#     print("Saabub kokkuvõte...")
#     print("See on soovitav toasoojus talvel")
# else:
#     print("something went wrong!")