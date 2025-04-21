import json

andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

# lisame failisse
with open("andmed.json", "r") as f:
    andmed_failist = json.load(f)
print(andmed_failist)

#loeme failist
with open("andmed.json", "w") as f:
    json.dump(andmed, f)
print(andmed_failist)

klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Juri", "hinne": 4}
]
}
with open("klass.json", "w", encoding = "utf-8-sig") as f:
    json.dump(klass, f, indent=2)

import requests

linn = input("Sisesta linna nimi: ")
api_voti = "1d1087e0fcd0b8b46d75a125f548f74e" # asenda oma API võtmega
url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
    peamine = andmed["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = andmed["weather"][0]["description"]
    tuul = andmed["wind"]["speed"]
    print(f"\nIlm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}°C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")
else:
    print("Linna ei leitud. Palun kontrolli nime õigekirja.")