from notificationservice import  NotificationService


class EmailNotificationService(NotificationService):
    def send(self, to, subject, body):
        print(f"Sending email to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")