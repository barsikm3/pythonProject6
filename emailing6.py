import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

port = 587
server = 'smtp.lesta.group'
user = 's_pasiukevich@lesta.group'
password = input("Type your password and press enter: ")

recipients = ['a_prakudzin@lesta.group', 'a_dyupon@lesta.group']
sender = 's_pasiukevich@lesta.group'
subject = 'Вы от нас уходите? Какая жаль'
text = 'Добрый день, ' \
       'Напоминаем, что в последний день вам надо побегать по этажам, движение - жизнь <b>да, прям побегать</b> fg совсем-совсем <h1> ну да</h1> бывают огорчения в жизни'
html = '<html><head></head><body><p>' + text + '</p></body></html>'

filepath = "scale_1200.jpeg"
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Python script <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/' + (python_version())

part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
part_file.set_payload(open(filepath, "rb").read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
encoders.encode_base64(part_file)

msg.attach(part_text)
msg.attach(part_html)
msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()