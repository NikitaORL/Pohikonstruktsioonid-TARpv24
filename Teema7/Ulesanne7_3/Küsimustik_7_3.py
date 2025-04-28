
from Teema7.Ulesanne7_3 import MyModule_küsimustik

while True:
    print("\n1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("3. Välju")

    valik = input("Vali tegevus (1-3): ")
    if valik == "1":
            MyModule_küsimustik.alusta_testi()
    elif valik == "2":
            MyModule_küsimustik.lisa_kysimus()
    elif valik == "3":
            print("Programmist väljutakse.")
            break
    else:
            print("Vale valik. Proovi uuesti.")