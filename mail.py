import smtplib, ssl
from readJSON import Myjson


class Mail:
    def __init__(self, local = False):

        port, sender_email, sender_pw = Myjson().credentials()
        self.port = port  # For SSL
        self.sender_email = sender_email
        self.password = sender_pw
        self.local = local
        if not local:
            self.smtp_server = "smtp.gmail.com"
        else:
            self.smtp_server = "localhost"
            self.port = 1025

    def sendMail(self, receiver_email, message):

        if self.local:        
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.sendmail(self.sender_email, receiver_email, message)
        else:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
