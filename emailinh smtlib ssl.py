import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

port = 587  # For starttls
smtp_server = "smtp.lesta.group"
sender_email = "s_pasiukevich@lesta.group"
receiver_email = "a_prakudzin@lesta.group"
password = input("Type your password and press enter: ")
message = """\ 
Проблема с кириллицей решена, будем дальше страдать :) 

"""
subject = 'Тестовое письмо, отправленное с питон-компилятора'
mime = MIMEText(message, 'plain', 'utf-8')
mime['Subject'] = Header(subject, 'utf-8')

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, mime.as_string())