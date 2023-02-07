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