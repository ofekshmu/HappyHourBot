import smtplib, ssl
import json


class Mail:
    def __init__(self, local=False):

        f = open('credentials.json')
        credentials = json.load(f)

        self.port = credentials['port']  # For SSL
        self.sender_email = credentials['sender mail']
        self.password = credentials['password']
        self.local = local
        if not local:
            self.smtp_server = "smtp.gmail.com"
        else:
            self.smtp_server = "localhost"
            self.port = 1025

    def sendMail(self, receiver_email, message=None):
        if message is None:
            message = self.message_obj
            self.message_obj['To'] = receiver_email

        if self.local:     
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.sendmail(self.sender_email, receiver_email, message)
        else:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
