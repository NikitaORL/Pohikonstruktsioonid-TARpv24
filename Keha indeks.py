print("Tere! Olen sinu uus s�ber - Python!")
nimi=input("Siseta oma nimi:")
print(f"{nimi} oi kui ilus nimi!")
try:
    soov=int(input(f"{nimi} Kas leian sinu keha indeksi? 0-ei, 1-jah => "))
    if soov==1:
        print("Indeksi leidmine...")
    elif soov==0:
        print("Kahju! See on v�ga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 v�i 0")
except:
    print("Vale soov!")

