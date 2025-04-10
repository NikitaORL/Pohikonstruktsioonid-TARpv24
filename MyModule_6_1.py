import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_eesti_vene(sona):
    if sona in sonastik:
        print(f"Tõlge vene keelde: {sonastik[sona]}")
    else:
        print("Sõna ei leitud sõnastikust.")

def tolgi_vene_eesti(sona):
    for est, rus in sonastik.items():
        if rus == sona:
            print(f"Tõlge eesti keelde: {est}")
            return
    print("Sõna ei leitud sõnastikust.")

def sona_lisamine():
    est = input("Sisesta uus sõna eesti keeles: ").strip()
    rus = input("Sisesta selle sõna vene tõlge: ").strip()
    if est in sonastik:
        print("See sõna on juba olemas.")
    else:
        sonastik[est] = rus
        print("Sõna lisatud!")

def sona_parandamine():
    vana_sona = input("Sisesta parandatav sõna (eesti keeles): ").strip()
    if vana_sona in sonastik:
        uus_sona = input("Sisesta uus eesti sõna: ").strip()
        uus_tolge = input("Sisesta uus vene tõlge: ").strip()
        del sonastik[vana_sona]
        sonastik[uus_sona] = uus_tolge
        print("Sõna parandatud!")
    else:
        print("Seda sõna ei leitud.")

def testi_teadmisi():
    print("Testi teadmisi alustatakse!")
    if not sonastik:
        print("Sõnastik on tühi.")
        return
    try:
        sonade_arv = int(input("Mitu sõna soovid testida? "))
    except ValueError:
        print("Palun sisesta arv.")
        return
    sonad = random.sample(list(sonastik.items()), min(sonade_arv, len(sonastik)))
    oiged = 0
    for est, rus in sonad:
        suund = random.choice(['est_rus', 'rus_est'])
        if suund == 'est_rus':
            vastus = input(f"Sisesta vene tõlge sõnale '{est}': ").strip()
            if vastus == rus:
                print("Õige!")
                oiged += 1
            else:
                print(f"Vale! Õige vastus: {rus}")
        else:
            vastus = input(f"Sisesta eesti tõlge sõnale '{rus}': ").strip()
            if vastus == est:
                print("Õige!")
                oiged += 1
            else:
                print(f"Vale! Õige vastus: {est}")
    protsent = round(oiged / len(sonad) * 100, 2)
    print(f"Test lõppenud! Sinu tulemus: {protsent}%")