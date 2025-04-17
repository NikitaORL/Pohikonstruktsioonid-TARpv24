
import smtplib, ssl
from email.message import EmailMessage
from tkinter import filedialog

def saada_kiri():
    kellele = input("Kellele saada: ")
    teema = input("Teema: ")
    # HTML контент
    sisu = '''<!DOCTYPE html>
<head>
</head>
<body>
    <h1>Sending an HTML email from Python</h1>
    <p>Hello there,</p>
    <a href="https://www.tthk.ee/">Here's a link to an awesome dev community!</a>
</body>
</html>'''

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "nikita.orlenko234@gmail.com"
    salasõna = input("Salasõna: ")  

    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = kellelt
    msg['To'] = kellele

    msg.set_content(sisu, subtype='html')

    fail = filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    if fail: 
        with open(fail, "rb") as f:
            fail_sisu = f.read()
            fail_nimi = fail.split("/")[-1]
            msg.add_attachment(fail_sisu, maintype="application", subtype="octet-stream", filename=fail_nimi)

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls(context=ssl.create_default_context())
                server.login(kellelt, salasõna)
                server.send_message(msg)
                print("Kiri saadetud edukalt!")
        except Exception as e:
            print("Viga:", e)

saada_kiri()