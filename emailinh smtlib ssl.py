import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


port = 587  # For starttls
smtp_server = "smtp.lesta.group"
sender_email = ""
receiver_email = ""
password = input("Type your password and press enter: ")
msg = MIMEMultipart()
msg['Subject'] = "Сервис по автоматической рассылке"
msg['From'] = "Приложение для рассылки писем сотрудникам"

# msg.attach(MIMEText(" как опшен для не для HTML "))
# with open("New Text Document.txt", "rb") as f:
    # file = MIMEApplication(f.read(), Name=basename("New Text Document.txt"))  это вариант для добавление txt файлов
# msg.attach(file)
# text = """"\
   # " " \
    #   
      # """


html = """\
<html>
  <body>
    <p>Добрый день,<br>
       
    </p>
  </body>
</html>
"""

part1 = MIMEApplication(open('ExTest.xlsx', 'rb').read())
part1.add_header('Content-Disposition', 'attachment', filename='ExTest.xlsx')
part2 = MIMEText(html, 'html')
part3 = MIMEApplication(open('scale_1200.jpeg', 'rb').read())
part3.add_header('Content-Disposition', 'attachment', filename='scale_1200.jpeg')
part4 = MIMEApplication(open('Тестовый документы Word.docx', 'rb').read())
part4.add_header('Content-Disposition', 'attachment', filename='Тестовый документы Word.docx')
part5 = MIMEApplication(open('bel.pdf', 'rb').read())
part5.add_header('Content-Disposition', 'attachment', filename='bel.pdf')
part6 = MIMEApplication(open('Presentation1.pptx', 'rb').read())
part6.add_header('Content-Disposition', 'attachment', filename='Presentation1.pptx')

msg.attach(part3)
msg.attach(part2)
msg.attach(part1)
msg.attach(part4)
msg.attach(part5)
msg.attach(part6)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
