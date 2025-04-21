import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Чтение вопросов и ответов из файла
def load_questions_and_answers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        questions = {}
        for line in file:
            question, answer = line.strip().split(":")
            questions[question] = answer
    return questions

# Генерация email адреса респондента
def generate_email(name):
    first_name, last_name = name.split()
    return f"{first_name.lower()}.{last_name.lower()}@example.com"

# Отправка письма респонденту
def send_email(to_email, subject, body):
    from_email = "your_email@example.com"
    password = "your_password"  # Не забудьте указать свой пароль!

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Замените на актуальные настройки SMTP
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Письмо отправлено на {to_email}")
    except Exception as e:
        print(f"Не удалось отправить письмо на {to_email}: {e}")

# Запуск анкеты для одного респондента
def conduct_survey(name, questions):
    print(f"\nПривет, {name}!")
    random_questions = random.sample(list(questions.items()), len(questions) // 2)  # Выбираем половину вопросов
    correct_answers = 0
    for question, correct_answer in random_questions:
        user_answer = input(f"{question}\nВаш ответ: ")
        if user_answer.strip().lower() == correct_answer.lower():
            correct_answers += 1
    return correct_answers

# Добавление нового вопроса
def add_new_question(filename):
    question = input("Введите новый вопрос: ")
    answer = input("Введите правильный ответ: ")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{question}:{answer}\n")
    print("Вопрос успешно добавлен.")

# Основная функция
def main():
    questions = load_questions_and_answers("kusimused_answers.txt")
    successful_respondents = []
    unsuccessful_respondents = []
    all_respondents = []
    
    M = int(input("Введите количество респондентов: "))
    
    for _ in range(M):
        name = input("Введите имя респондента: ")
        email = generate_email(name)
        
        if any(name == r[0] for r in all_respondents):
            print(f"Респондент {name} уже проходил анкетирование.")
            continue
        
        correct_answers = conduct_survey(name, questions)
        all_respondents.append((name, correct_answers, email))
        
        if correct_answers > len(questions) // 4:  # Больше половины
            successful_respondents.append((name, correct_answers, email))
        else:
            unsuccessful_respondents.append((name, correct_answers, email))
        
        # Отправка письма респонденту
        subject = "Результаты анкеты"
        if correct_answers > len(questions) // 4:
            body = f"Привет {name}! Ваше количество правильных ответов: {correct_answers}. Вы успешно прошли тест."
        else:
            body = f"Привет {name}! Ваше количество правильных ответов: {correct_answers}. К сожалению, вы не прошли тест."
        send_email(email, subject, body)

    # Сохранение успешных респондентов
    with open("oiged.txt", "w", encoding="utf-8") as file:
        for name, correct_answers, _ in sorted(successful_respondents, key=lambda x: x[1], reverse=True):
            file.write(f"{name} - {correct_answers} правильных\n")
    
    # Сохранение неуспешных респондентов
    with open("wrong.txt", "w", encoding="utf-8") as file:
        for name, correct_answers, _ in sorted(unsuccessful_respondents, key=lambda x: x[0]):
            file.write(f"{name} - {correct_answers} правильных\n")
    
    # Сохранение всех респондентов
    with open("koik.txt", "w", encoding="utf-8") as file:
        for name, correct_answers, email in all_respondents:
            file.write(f"{name} - {correct_answers} правильных - {email}\n")

    # Отправка отчета работодателю
    subject = "Отчет о результатах анкетирования"
    body = "Здравствуйте!\n\nСегодняшние результаты анкетирования:\n"
    
    best_respondent = None
    best_score = 0
    
    for i, (name, correct_answers, email) in enumerate(all_respondents, 1):
        result = "СОБИС" if correct_answers > len(questions) // 4 else "НЕ ПОДХОДИТ"
        body += f"{i}. {name} - {correct_answers} правильных - {email} - {result}\n"
        if correct_answers > best_score:
            best_score = correct_answers
            best_respondent = name
    
    body += f"\nЛучший респондент: {best_respondent} ({best_score} правильных)\n\nС уважением,\nПрограмма автоматизации анкетирования"
    send_email("tootaja@firma.ee", subject, body)
    
    print("\nРезультаты отправлены на адреса электронной почты.")

# Главный цикл программы
if __name__ == "__main__":
    while True:
        print("\n1. Начать анкету")
        print("2. Добавить новый вопрос")
        print("3. Выйти")
        choice = input("Выберите опцию: ")
        
        if choice == "1":
            main()
        elif choice == "2":
            add_new_question("kusimused_answers.txt")
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")