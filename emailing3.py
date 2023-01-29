import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


sender_email = "s_pasiukevich@lesta.group"
receiver_email = "barsik2gtii@yandex.ru"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Решил срулить с галеры? Тогда не забудь сделать файнал трип эраунд зэ офис"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Добрый день,
How are you?
Напоминаем, что в последний день в Минском офисе дд/мм/гггг вам нужно подойти
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Добрый день,<br>
       Напоминаем, что в последний день в Минском офисе дд/мм/гггг вам нужно подойти туда<br>
       в Волну в 925 кабинет (Staff Records)<br>
       и вот сюда ас велл<br>
       <a href="https://lesta.ru/ru">Лестовики</a>  
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
part3 = MIMEApplication(open('scale_1200.jpeg', 'rb').read())
part3.add_header('Content-Disposition', 'attachment', filename='scale_1200.jpeg')
message.attach(part3)

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.lesta.group", 587, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())