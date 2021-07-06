import smtplib, ssl
import pickle
import os

from robin_monitor.settings import Settings

class Notifier(Settings):

    def __init__(self, user):
        super(Notifier, self).__init__()
        self.user = user


class EmailNotifier(Notifier):

    def __init__(self, user):
        super(EmailNotifier, self).__init__(user)
        self.port = 465
        self.server_smtp = None
        self.email = self.user.email
        self.password = self.user.email_password

    def set_smtp_server(self, server):
        self.server_smtp = server

    def send_email(self, subject, body):
        port = self.port  # For SSL
        message = \
            """Subject: {}
            \n
            {}
            """.format(subject, body)
    
        # Create a secure SSL context
        context = ssl.create_default_context()
    
        with smtplib.SMTP_SSL(self.server_smtp, port, context=context) as svr_obj:
            svr_obj.login(self.email, self.password)
            svr_obj.sendmail(self.email, self.email, message)


class GmailNotifier(EmailNotifier):
    
    def __init__(self, user):
        super(GmailNotifier, self).__init__(user)
        self.server_smtp = "smtp.gmail.com"
    