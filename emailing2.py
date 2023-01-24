import zmail
server = zmail.server('barsik2gtii@yandex.ru', 'QWghbynth17')

# Send mail
server.send_mail('a_prakudzin@lesta.group',{'subject':'Код для рассылки готов:)','content_text':'Тестовый код by Python масс рассылка'})
# Or to a list of friends.
server.send_mail(['n_gulko@lesta.group','s_pasiukevich@lesta.group'],{'subject':'Код для рассылки готов','content_text':'Тестовый код by Python масс рассылка'})

# Retrieve mail
latest_mail = server.get_latest()
zmail.show(latest_mail)