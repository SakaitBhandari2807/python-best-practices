from patterns.structural.adapter_pattern.notificationservice import NotificationService
from patterns.structural.adapter_pattern.emailnotificationservice import EmailNotificationService
from patterns.structural.adapter_pattern.sendgridservice import SendGridService
from patterns.structural.adapter_pattern.SendGridAdapter import SendGridAdapter

if __name__ == "__main__":
    emailService: NotificationService = EmailNotificationService()
    emailService.send("customer@alphabet.com", 'orderConfirmation', 'your order has been received')

    gridService: SendGridService = SendGridService()
    emailServiceGrid: NotificationService = SendGridAdapter(gridService)

    emailServiceGrid.send("customer@alphabet.com", 'orderConfirmation', 'your order has been received')
