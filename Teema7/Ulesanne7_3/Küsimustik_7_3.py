import random
import smtplib
from email.message import EmailMessage
import ssl


# Отправка email-уведомления
def send_email_notification(email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    sender_email = "nikita.orlenko234@gmail.com"       # ← сюда вставь свой email
    sender_password = "ikar dwvb gqpa ggpc"    # ← сюда вставь свой пароль приложения

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email успешно отправлен.")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")


# Генерация email по имени, если пользователь ничего не ввёл
def loo_email(nimi):
    osad = nimi.lower().split()
    if len(osad) == 2:
        return f"{osad[0]}.{osad[1]}@example.com"
    return nimi.replace(" ", ".").lower() + "@example.com"


# Чтение вопросов и ответов из файла
def loe_kusimused():
    kys_vas = {}
    with open("Teema7//Ulesanne7_3//kusimused_ja_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            if ":" in rida:
                osad = rida.strip().split(":", 1)
                kysimus = osad[0].strip()
                vastus = osad[1].strip()
                kys_vas[kysimus] = vastus
    return kys_vas


# Основная функция запуска тестирования
def alusta_testi():
    kysimused = loe_kusimused()
    kasutajad = []
    M = 3  # Кол-во участников
    N = 5  # Кол-во вопросов

    for i in range(M):
        print(f"\nTestija {i + 1}")
        nimi = input("Sisesta oma nimi (Eesnimi Perenimi): ")
        email = input("Sisesta oma e-posti aadress (või jäta tühjaks): ")
        if not email:
            email = loo_email(nimi)

        if nimi in kasutajad:
            print("Selle nimega on juba test tehtud.")
            continue
        kasutajad.append(nimi)

        kysimused_list = list(kysimused.items())
        random.shuffle(kysimused_list)
        valitud = kysimused_list[:N]

        oiged = 0
        for kysimus, oige in valitud:
            vastus = input(kysimus + " ")
            if vastus.strip().lower() == oige.lower():
                oiged += 1

        tulemus_rida = f"{nimi} – {oiged} õigesti"

        # Сохраняем в нужный файл
        if oiged >= (N // 2 + 1):
            with open("Teema7//Ulesanne7_3//oiged_vastused.txt", "a", encoding="utf-8") as f:
                f.write(tulemus_rida + "\n")
            seis = "Sa sooritasid testi edukalt."
        else:
            with open("Teema7//Ulesanne7_3//Vale_vastused.txt", "a", encoding="utf-8") as f:
                f.write(nimi + "\n")
            seis = "Kahjuks testi ei sooritatud edukalt."

        with open("Teema7//Ulesanne7_3//koik_inimised.txt", "a", encoding="utf-8") as f:
            f.write(f"{nimi} – {oiged} – {email}\n")

        # Отправка результата пользователю
        subject = "Küsimustiku tulemus"
        body = f"Tere {nimi}!\nSinu õigete vastuste arv: {oiged}.\n{seis}"
        send_email_notification(email, subject, body)

    print("\nKõik testid on tehtud.")
    print("Tulemused saadetud e-posti aadressidele.")


# Добавление нового вопроса
def lisa_kysimus():
    uus = input("Sisesta uus küsimus: ")
    vastus = input("Sisesta õige vastus: ")
    with open("Teema7//Ulesanne7_3//kusimused_ja_vastused.txt", "a", encoding="utf-8") as f:
        f.write(f"{uus}:{vastus}\n")
    print("Küsimus lisatud!")


# Меню выбора
def menuu():
    while True:
        print("\n1. Alusta küsimustikku")
        print("2. Lisa uus küsimus")
        print("3. Välju")

        valik = input("Vali tegevus (1-3): ")
        if valik == "1":
            alusta_testi()
        elif valik == "2":
            lisa_kysimus()
        elif valik == "3":
            print("Programmist väljutakse.")
            break
        else:
            print("Vale valik. Proovi uuesti.")

menuu()