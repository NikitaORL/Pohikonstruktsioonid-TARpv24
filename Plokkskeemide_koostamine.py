# print("Tere, täna tahaksin kindlaks teha pangas hoitud summa!")
# Y = float(input("Palun ütle mulle esialgse deposiidi summa"))
# H = float(input("ütle mulle, mitu aastat oli tagatisraha"))
# Z = float(input("kui suur oli hoiuse aastane intress?"))
# T = Y * (1 + Z / 100) ** H
# print(f"Pangas kogunenudsumma on {T} eurot!")
# --------------------------------------------------------------

#V4. 2  Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.

# vastus=0
# P=int(input("Mitu korda kordame?"))
# for i in range(P):
#     arv=float(input("Sisesta arv: "))
#     if arv<0: vastus+=arv
#     P-=1
#     if P==0: break
# print(f"Summa on: {vastus}")

#V1. 4 Koostage plokkskeem kotlette praadiva roboti jaoks.
kokku = 100
panni_maht = 6
aeg = 1
kokkuu = 0
for a in range (0, 100, 6):
    if a > 0:
        kokkuu += 6
        kokku -= 6
        aeg += 1
        print(f"Ma tegin {kokkuu} kotlette")