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
    selection = results_list.curselection()
    if selection:
        selected_value = results_list.get(selection[0])
        select_data.set(selected_value)


def load_file(*args):
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    results_list["height"] = min(10, df.shape[0])

def send_email(*args):
    # Set up email parameters
    from_address = input("input your email:")
    to_address = input(f"{select_data}")
    password = input("input your password:")
    subject = "Excel Data"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Select attachments
    root.filename = \
        filedialog.askopenfilenames(initialdir = "/", title = "Select files", filetypes =
        (("all files","*.*"),("jpeg files","*.jpg"),("png files","*.png"),("pdf files","*.pdf"),("text files","*.txt")))
    for file in root.filename:
        with open(file, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition",f"attachment; filename={file}")
        msg.attach(part)

    # Send the email
    server = smtplib.SMTP("smtp.yandex.ru", 465)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()


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

root.mainloop()