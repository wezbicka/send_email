import smtplib
import os


host = 'smtp.yandex.ru:465'
sender_email = os.environ['SENDER_EMAIL']
recipient_email = os.environ['RECIPIENT_EMAIL']
website = "https://dvmn.org/referrals/VrjIagsf9uZu2MEZcEWgO9vbOYpTjryN4mwkjmbX/"
friend_name = "Нурбек"
my_name = "Полина"
password = os.environ['MAIL_PASSWORD']
template = """\
From: {sender_email}
To: {recipient_email}
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8"; 

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!
  
{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 
  
Как будет проходить ваше обучение на {website}? 
  
  → Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
  → Будешь учиться без стресса и бессонных ночей. 
  Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
  → Подготовишь крепкое резюме.
  Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
  
  Регистрируйся → {website}  
  На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
letter = template.format(
    sender_email=sender_email,
    recipient_email=recipient_email,
    website=website,
    friend_name=friend_name,
    my_name=my_name,
)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL(host)
server.login(sender_email, password)
server.sendmail(sender_email, recipient_email, letter)
server.quit()
