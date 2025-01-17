import os
import requests
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

DEPATURE_AIRPORT_CODE = 'IAD'
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._account_id = os.getenv("ACCOUNT_SID")
        self._auth_token = os.getenv("AUTH_TOKEN")
        self.sender_number = os.getenv("TWILIO_NUMBER")
        self.receiver_number = os.getenv("VERIFIED_NUMBER")
        self.my_mail = os.getenv("MY_MAIL")
        self.secret_key = os.getenv("MY_PASSWORD")
                
    def send_message(self, current_price, price, a_airport, out_date, in_date, stops, carriers_name):
        """Function to send a Whatsapp message with the current price, price, arrival airport, and flight dates."""
        #Uncomment to send message to whatsapp
        if float(current_price) < float(price):
            client = Client(self._account_id, self._auth_token)

            message = client.messages.create(
            from_=f"whatsapp:{self.sender_number}",
            body=f"Low price alert! only ${current_price} to fly from {DEPATURE_AIRPORT_CODE} to {a_airport}, "
            f"with only {stops} stop(s) ({carriers_name}) on {out_date} until {in_date}",
            to=f"whatsapp:{self.receiver_number}"
            )
            print(message.status)

    def send_email(self, emails, current_price, price, a_airport, out_date, in_date, stops, carriers_name):  
        """Function to send an email notification with the current price, price, arrival airport, and flight dates."""
        if float(current_price) < float(price):
            for email in emails:
                with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                    connection.starttls()
                    connection.login(self.my_mail, self.secret_key)
                    self.message = f"Only ${current_price} to fly from {DEPATURE_AIRPORT_CODE} to {a_airport}, with only {stops} stop(s) ({carriers_name}) on {out_date} until {in_date}"
                    connection.sendmail(self.my_mail, email, msg=f'Subject: Low Price Alert!\n\n{self.message}')
