import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

DEPATURE_AIRPORT_CODE = 'IAD'
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, current_price, price, a_airport, out_date, in_date):
        """Function to send an email notification with the current price, price, arrival airport, and flight dates."""
        self._account_id = os.getenv("ACCOUNT_SID")
        self._auth_token = os.getenv("AUTH_TOKEN")
        self.sender_number = os.getenv("TWILIO_NUMBER")
        self.receiver_number = os.getenv("VERIFIED_NUMBER")
        
        if float(current_price) < float(price):
            client = Client(self._account_id, self._auth_token)

            message = client.messages.create(
            from_=f"whatsapp:{self.sender_number}",
            body=f"Low price alert! only ${current_price} to fly from {DEPATURE_AIRPORT_CODE} to {a_airport},"
            f"on {out_date} until {in_date}",
            to=f"whatsapp:{self.receiver_number}"
            )
            print(message.status)
        
        
        
    