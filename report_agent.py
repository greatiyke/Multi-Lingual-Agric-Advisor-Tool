from services.messaging_service import MessagingService

class ReportAgent:
    def __init__(self):
        self.messaging_service = MessagingService()

    def send_report(self, recipient_number, advice):
        result = self.messaging_service.send_message(recipient_number, advice)
        return result
