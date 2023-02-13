import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd
import tkinter as tk
from tkinter import messagebox, OptionMenu
from tkinter import filedialog
from tkinter import ttk


def search(*args):
    input = select_data.get()
    if len(input) < 2:
        return
    matching = []
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            cell_value = df.iloc[i, j]
            if input in str(cell_value):
                matching.append((i, cell_value))
    results_list.delete(0, tk.END)
    for i, e in matching:
        results_list.insert(tk.END, f"{e}")


def select_email(*args):
    global selected_value
    selection = results_list.curselection()
    if selection:
        selected_value = results_list.get(selection[0])
        select_data.set(selected_value)


def load_file(*args):
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    results_list["height"] = min(10, df.shape[0])

def create_new_list():
    selected_value = select_data.get()
    print(selected_value)
    return selected_value


def send_email():
    port = 587  # For starttls
    smtp_server = "smtp.lesta.group"
    sender_email = email_entry.get()
    receiver_email = create_new_list()
    password = password_entry.get()
    msg = MIMEMultipart()
    msg['Subject'] = "Сервис по автоматической рассылке"
    msg['From'] = "Приложение для рассылки писем сотрудникам"
    html = """\
    <html>
      <body>
        <p>Добрый день,<br>
           Напоминаем, что в последний день в Минском офисе дд/мм/гггг вам нужно подойти туда<br>
           в Волну в 925 кабинет (Staff Records)<br>
           и вот сюда <br>
           <a href="https://lesta.ru/ru">Лестовики</a>  
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
        exit(0)

def check_password(value):
    password = password_entry.get()
    if password == "secret":
        messagebox.showinfo("Correct", "Password is correct")
    else:
        messagebox.showinfo("Incorrect", "Password is incorrect")
        exit(0)
root = tk.Tk()
root.title("Excel Data Selector")

html = tk.Text(root, height=10, width=50)
html.pack()
html.config(state="normal")
html.insert(tk.END, "This text")
html.tag_add("redact", "1.0", tk.END)
html.tag_config("redact", foreground="black", background="white")

# Create a tkinter button to trigger the function to send email
password_label = tk.Label(root, text="Password")
password_entry = tk.Entry(root, show="*")
email_label = tk.Label(root, text="Put your email")
email_entry = tk.Entry(root, show="")
#email_sending = tk.Label(root, text="Receiver of the email")
#email_sending = tk.Entry(root, show="")
menu = ttk.OptionMenu(root, tk.StringVar(), *["Check"], command=check_password)

send_button = tk.Button(root, text="Send Email", command=send_email)

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)


results_list = tk.Listbox(root, height=10)
results_list.pack(pady=25)
results_list.bind("<Button-1>", select_email)

load_button = tk.Button(root, text="Load Excel File", command=load_file)
load_button.pack(pady=10)

create_new_list_button = tk.Button(root, text="Choosen Email", command=create_new_list)
create_new_list_button.pack()


email_label.pack()
email_entry.pack()
 # email_sending.pack()
password_label.pack()
password_entry.pack()
send_button.pack()

# Start tkinter GUI event loop
root.mainloop()
root.quit()