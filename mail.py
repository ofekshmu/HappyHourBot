import smtplib, ssl



class Mail:
    def __init__(self, port, sender_email, sender_pw):

        # self.port = port
        # self.sender_email = sender_email
        # self.sender_pw = sender_pw

        self.port = 465  # For SSL
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = "meshulavim14@gmail.com"  # Enter your address
        self.password = "lmquobcbwgocuwrs"

    def sendMail(self, receiver_email, message):

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)
