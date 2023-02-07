import tkinter as tk
from tkinter import filedialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(*args):
    # Set up email parameters
    from_address = entry_from.get()
    to_address = select_data.get()
    password = entry_pwd.get()
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
root.title("Send Email")

label_from = tk.Label(root, text="From:")
label_from.grid(row=0, column=0, pady=10)

entry_from = tk.Entry(root)
entry_from.grid(row=0, column=1, pady=10)

label_pwd = tk.Label(root, text="Password:")
label_pwd.grid(row=1, column=0, pady=10)

entry_pwd = tk.Entry(root, show="*")
entry_pwd.grid(row=1, column=1, pady=10)

select_data = tk.Entry(root)
select_data.grid(row=2, column=1, pady=10)

button = tk.Button(root, text="Send", command=send_email)
button.grid(row=3, column=1, pady=10)

root.mainloop()
