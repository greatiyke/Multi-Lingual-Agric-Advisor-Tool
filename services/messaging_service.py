import os
from twilio.rest import Client

class MessagingService:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("TWILIO_FROM_NUMBER")
        
        if self.account_sid and self.auth_token:
            self.client = Client(self.account_sid, self.auth_token)
        else:
            self.client = None

    def send_message(self, to_number, message):
        print(f"[MessagingService] Sending SMS to {to_number}...")
        
        if not self.client:
            print("[MessagingService] Error: Twilio credentials missing.")
            return {"status": "failed", "error": "Credentials missing"}

        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            return {"status": "sent", "sid": message.sid}
        except Exception as e:
            print(f"[MessagingService] Error sending SMS: {e}")
            return {"status": "failed", "error": str(e)}
