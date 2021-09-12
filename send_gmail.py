import smtplib
import os
from email.mime.text import MIMEText


def send_mail(subject: str, message: str):
    sender = 'from_address'
    password = os.getenv('EMAIL_PASSWORD')
    addressee = 'to_address'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)  # cyrillic support
        msg['Subject'] = subject
        server.sendmail(sender, addressee, msg.as_string())

        return 'The message was sent successfully'

    except Exception as ex:
        return f'{ex}\nCheck your login or password please!'


def main():
    subject = input('Type message subject: ')
    message = input('Type your message: ')
    print(send_mail(subject, message))


if __name__ == '__main__':
    main()
