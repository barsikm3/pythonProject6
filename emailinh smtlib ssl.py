import smtplib, ssl
from email.mime.text import MIMEText

port = 587  # For starttls
smtp_server = "smtp.lesta.group"
sender_email = "s_pasiukevich@lesta.group"
receiver_email = "a_dyupon@lesta.group"
password = input("Type your password and press enter: ")
message = """\
Subject: Вы покидаете нашу компанию? Скатертью дорожка
Добрый день, 
Напоминаем, что в последний день в Минском офисе дд/мм/гггг Вам нужно подойти в Волну, 925 каб (Staff Records – кадры) в 10.30 -11.00, для подписания необходимых документов и получения трудовой книжки. 
До этой даты, с вами свяжутся сотрудники команды Service Desk и предоставят список оборудования, которое необходимо сдать. Технику необходимо доставить в офис в день увольнения не позднее 10 часов утра. Если есть какие-либо вопросы по сдаче техники, вы сможете непосредственно уточнить с ними. 
Расчет поступит в этот же день на Вашу банковскую карту;
Корпоративный пропуск нужно сдать на посту охраны Волны.
При возникновении вопросов, обращайтесь по адресу блаблабла"""

msg = MIMEText(message)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)