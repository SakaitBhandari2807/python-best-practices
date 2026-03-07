from notificationservice import NotificationService
from sendgridservice import SendGridService


class SendGridAdapter(NotificationService):

    def __init__(self, sendGridService : SendGridService):
        self.sendgridservice = sendGridService

    def send(self, to: str, subject: str, body: str):
        self.sendgridservice.send_email(to, subject, body)