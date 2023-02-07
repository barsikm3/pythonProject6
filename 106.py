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