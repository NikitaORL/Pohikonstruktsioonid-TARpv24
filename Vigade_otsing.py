# 1. Muutsin "import * from math" "import math"-iks, et kasutada "math.sqrt"
import math
print("Ruudu karakteristikud")
while True:
    a=input('Sisesta ruudu külje pikkus => ')
    try:
        a = float(a)
        if (a <= 0):
            print("Pikkus peab olema suurem kui 0")
            continue
        break
    except:
        print("Palun sisesta õige number")

S=a**2
print("Ruudu pindala", S)
P=4*a
# 2. Muutsin '' asemel " kasutamiseks
print("Ruudu ümbermõõt", P)
# 3. Funktsiooni nime viga, muutsin "sqr" "sqrt"-iks
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
# 4. Eemaldasin liigse ")"
print("Ristküliku karakteristikud")
while True:
    b=input("Sisesta ristküliku 1. külje pikkus => ")
    c=input("Sisesta ristküliku 2. külje pikkus => ")
    try:
        b = float(b)
        c = float(c)
        if (b <= 0 or c <= 0):
            print("Pikkus peab olema suurem kui 0")
            continue
        break
    except:
        print("Palun sisesta õige number")

S=b*c
# 5. Lisatud ' algusesse
print('Ristküliku pindala', S)
# 6. Lisasin * korrutamiseks
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
# 7 Muutsin kõik * väärtuseks **
di=math.sqrt(b**2+c**2)
# 8. Lisan ")" lõppu ja ühe koha pärast koma
print("Ristküliku diagonaal", round(di, 1))
print()
print("Ringi karakteristikud")
 #9. Muutsin kõik '' väärtuseks " ja eemaldasins liigse ")"
while True:
    r=input("Sisesta ringi raadiusi pikkus => ")
    try:
        if (r <= 0):
            print("Raadius peab olema suurem kui 0")
            continue
        r = float(r)
        break
    except:
        print("Palun sisesta õige number")

# 10. lisasin * 
d=2*r ,
print("Ringi läbimõõt", d)
# 11. Muutsin pi() math.pi-ks
# 12. Muutsin "r*2" väärtuseks "r**2"
S=math.pi*r**2
# 13. Lisan 2 kohta pärast koma
print("Ringi pindala", round(S, 2))
# Lisasin * korrutamiseks, muutsin pi() math.pi-ks
C=2 * math.pi * r
# 14. Lisasin ")" lõppu
print("Ringjoone pikkus", round(C, 2))


