import smtplib
from email.mime.text import MIMEText

EMAIL = "yourgmail@gmail.com"
PASSWORD = "your_app_password"

def send_email(receiver, subject, message):

    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = receiver

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.sendmail(EMAIL, receiver, msg.as_string())

    server.quit()