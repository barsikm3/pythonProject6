import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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


def send_email(*args):
    email = select_data.get()
    password = "YOUR_PASSWORD"
    to = email
    subject = "Test email"
    message = "This is a test email sent from python."
    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, to, text)
    server.quit()
    print("Email sent successfully.")


def load_file(*args):
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    results_list["height"] = min(10, df.shape[0])


root = tk.Tk()
root.title("Autocomplete Search")

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)


results_list = tk.Listbox(root, height=10)
results_list.pack(pady=25)
results_list.bind("<Button-1>", select_email)

load_button = tk.Button(root, text="Load Excel File", command=load_file)
load_button.pack(pady=10)

send_button = tk.Button(root, text="Send Email", command=send_


