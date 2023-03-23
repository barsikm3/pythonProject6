import zmail
server = zmail.server('', '')

# Send mail
server.send_mail('',{'subject':'По сообщению в вк тимс:)','content_text':'ахахах :) '})
# Or to a list of friends.
#server.send_mail(['n_gulko@lesta.group','s_pasiukevich@lesta.group'],{'subject':'Код для рассылки готов','content_text':'Тестовый код by Python масс рассылка'})

# Retrieve mail
latest_mail = server.get_latest()
zmail.show(latest_mail)
