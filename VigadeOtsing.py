# Ma muutsin "import * from math" käsu "import math"-iks, et kasutada funktsiooni math.sqrt.
#--------------------------------------------------------------------------------------------------
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

# Ma muutsin ülakomade ('') asemel jutumärkide (") kasutamise.
#--------------------------------------------------------------------------------------------------

print("Ruudu ümbermõõt", P)

# Parandasin funktsiooni nime vea, muutes "sqr" "sqrt"-iks.
#--------------------------------------------------------------------------------------------------

di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()

# Kustutasin üleliigse ) sümboli.
#--------------------------------------------------------------------------------------------------

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

# Lisasin ülakoma ('') algusesse.
#--------------------------------------------------------------------------------------------------

print('Ristküliku pindala', S)

# Lisasin * korrutamise jaoks.
#--------------------------------------------------------------------------------------------------

P=2*(b+c)
print("Ristküliku ümbermõõt", P)

# Asendasin kõik * sümbolid **-ga.
#--------------------------------------------------------------------------------------------------

di=math.sqrt(b**2+c**2)

# Lisain lõppu ) ja ühe koha pärast koma.
#--------------------------------------------------------------------------------------------------

print("Ristküliku diagonaal", round(di, 1))
print()
print("Ringi karakteristikud")

 # Asendasin kõik ülakomad ('') jutumärkidega (") ja eemaldasin üleliigse ).
 #--------------------------------------------------------------------------------------------------

while True:
    r=int(input("Sisesta ringi raadiusi pikkus => ")) #lisasin "int"
    try:
        if (r <= 0):
            print("Raadius peab olema suurem kui 0")
            continue
        r = float(r)
        break
    except:
        print("Palun sisesta õige number")

# Lisasin korrutamismärgi *.
#--------------------------------------------------------------------------------------------------

d=2*r ,
print("Ringi läbimõõt", d)

# Asendasin pi() väärtusega math.pi.
# Muutsin "r*2" väärtuseks "r**2".
#--------------------------------------------------------------------------------------------------

S=math.pi*r**2

# Lisasin kaks kohta pärast koma.
#--------------------------------------------------------------------------------------------------

print("Ringi pindala", round(S, 2))

# Lisasin * korrutamise jaoks ja asendasin pi() väärtusega math.pi.
#--------------------------------------------------------------------------------------------------

C=2 * math.pi * r

# Lisasin lõppu ).
#--------------------------------------------------------------------------------------------------

print("Ringjoone pikkus", round(C, 2))
