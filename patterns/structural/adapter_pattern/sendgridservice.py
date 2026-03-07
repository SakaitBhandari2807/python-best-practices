class SendGridService:
    def send_email(self, recipient: str, subject: str, content: str):
        print(f"Sending email via sendgrid to {recipient}")
        print(f"Subject: {subject}")
        print(f"Content: {content}")

