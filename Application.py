import pandas as pd
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import filedialog
from tkinter import ttk

# Read data from excel file
df = pd.read_excel('Book23.xlsx')

# Create tkinter GUI window
root = tk.Tk()
root.title("Excel Data Selector")

# Create a ttk Combobox to select data
select_data = ttk.Combobox(root, values=df['Email'].tolist(), state='normal')
select_data.pack()

lst = ['']

# Function to display selected data
def show_data(event):
    value = event.widget.get()
    if value == '':
        combo_box['value'] = lst
    selected = select_data.get()
    data = df.loc[df['column_name'] == selected]
    print(data)

# Function to send an email with attachments
def send_email():
    # Set up email parameters
    from_address = "youremail@example.com"
    to_address = "recipientemail@example.com"
    password = "yourpassword"
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
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

# Create a tkinter button to trigger the function to show data
button_show = tk.Button(root, text="Email", command=show_data)
button_show.pack()

# Create a tkinter button to trigger the function to send email
button_email = tk.Button(root, text="Send Email", command=send_email)
button_email.pack()

# Start tkinter GUI event loop
root.mainloop()