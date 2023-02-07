import tkinter as tk
import smtplib

def send_email(recipient):
    # Replace the following values with your own email account details
    sender = 'youremail@example.com'
    password = 'yourpassword'
    message = 'Subject: Test Email\n\nThis is a test email sent from Python.'

    server = smtplib.SMTP('smtp.example.com', 587) # Replace with your own SMTP server details
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()

def on_value_selected(event):
    recipient = combobox.get()
    send_email(recipient)

root = tk.Tk()
combobox = tk.ttk.Combobox(root, values=['email1@example.com', 'email2@example.com', 'email3@example.com'])
combobox.bind('<<ComboboxSelected>>', on_value_selected)
combobox.pack()
root.mainloop()


