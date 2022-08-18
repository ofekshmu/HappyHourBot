import smtplib, ssl
import readJSON


class Mail:
    def __init__(self):

        port, sender_email, sender_pw = readJSON().credentials()
        self.port = port  # For SSL
        self.sender_email = sender_email
        self.password = sender_pw

        self.smtp_server = "smtp.gmail.com"

    def sendMail(self, receiver_email, message):

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)
