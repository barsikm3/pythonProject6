import smtplib
import ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


port = 587  # For starttls
smtp_server = "smtp.lesta.group"
sender_email = "s_pasiukevich@lesta.group"
receiver_email = "i_hauryliuk@lesta.group"
password = input("Type your password and press enter: ")
msg = MIMEMultipart()

# msg.attach(MIMEText("Ты считаешь, что если я холодная - я безчувственная и невкусная? Все, Дюпончик, вражда навеки "))
# with open("New Text Document.txt", "rb") as f:
    # file = MIMEApplication(f.read(), Name=basename("New Text Document.txt"))
# msg.attach(file)
text = """"\
    "Чыки бамбони " \
       "Напоминаем, что в последний день в Минском офисе дд/мм/гггг вам нужно подойти туда " \
       "в Волну в 925 кабинет (Staff Records) " \
       "и вот сюда ас велл " \
       """


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

msg['Subject'] = "Корпоративная приблуда"
msg['From'] = "Решил срулить с галеры? Аста ла виста, детка"

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
part3 = MIMEApplication(open('scale_1200.jpeg', 'rb').read())
part3.add_header('Content-Disposition', 'attachment', filename='scale_1200.jpeg')

msg.attach(part3)
msg.attach(part2)
msg.attach(part1)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())