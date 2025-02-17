
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Siseta oma nimi:")
print(f"{nimi} oi kui ilus nimi!")
while 1:
    try:
        soov=int(input(f"{nimi} Kas leian sinu keha indeksi? 0-ei, 1-jah => "))
        if soov==1:
            print("Indeksi leidmine...")
            try:
                pikkus=int(input("Mis on sinu pikkus?"))
                try:
                    mass=float(input("Mis on sinu kaal?"))
                    indeks=mass/(0.1*pikkus)**2
                    print(f"{nimi}, sinu keha indeks on: {indeks}")
                    if indeks < 16:
                        print("Tervisele ohtlik alakaal")
                    elif indeks==16-19:
                        print("Alakaal")
                    elif indeks==19 - 25:
                        print("Normaalkaal")
                    elif indeks==25 - 30:
                        print("Ülekaal")
                    elif indeks==30 - 35:
                        print("Rasvumine")
                    elif indeks==35 - 40:
                        print("Tugev rasvumine")
                    elif indeks>40:
                        print("Tervisele ohtlik rasvumine")
                        break
                except:
                    print("Vale kaalu formaat!")
            except:
                print("Vale pikkuse formaat!")
        elif soov==0:
            print("Kahju! See on väga kasulik info!")
            break
        else:
            print("Vale valik. Saab valida ainult 1 või 0")
    except:
        print("Vale soov!")