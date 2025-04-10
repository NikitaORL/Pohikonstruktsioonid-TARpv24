from MyModule_6_1 import *

def alustamine():
    print("Tere tulemast eesti-vene sõnastikku!")
    while True:
        print("\nValikud:")
        print("1 - Tõlgi eesti -> vene")
        print("2 - Tõlgi vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")

        valik = input("Tee oma valik: ").strip()
        if valik == '1':
            sona = input("Sisesta sõna eesti keeles: ").strip()
            tolgi_eesti_vene(sona)
        elif valik == '2':
            sona = input("Sisesta sõna vene keeles: ").strip()
            tolgi_vene_eesti(sona)
        elif valik == '3':
            sona_lisamine()
        elif valik == '4':
            sona_parandamine()
        elif valik == '5':
            testi_teadmisi()
        elif valik == '6':
            print("Head aega!")
            break
        else:
            print("Tundmatu valik, proovi uuesti.")

alustamine()