import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.end_log = os.getenv('ENDPOINT_LOG')
        self.auth_key = os.getenv('AUTHORIZATION_KEY')
        self.header = {'Authorization': f'{self.auth_key}'}
        self.price_endpoint = f'https://api.sheety.co/{self.end_log}/flightDeals/prices'
        self.user_endpoint = f'https://api.sheety.co/{self.end_log}/flightDeals/users'
        self.user_list = []

    def get_data(self):
        # This method fetches price data from the Google Sheet.
        self.response = requests.get(self.price_endpoint, headers=self.header)
        self.data = self.response.json()
        self.prices = self.data['prices']
        return self.prices
    
    def get_customer_emails(self):
        # This method fetches user emails from the Google Sheet.
        self.response = requests.get(self.user_endpoint, headers=self.header)
        self.data = self.response.json()
        self.users = self.data['users']
        for user in self.users:
            self.user_list.append(user['whatIsYourEmail?'])  # Extracting user emails for sending emails.
        return self.user_list

    def update_data(self, row_id, iata_code):
        # This method updates the iata_code field for a given city
        SHEERTY_PUT_ENDPOINT = f"{self.price_endpoint}/{row_id}"
        data = {
            "price": {
                "iataCode": iata_code,
            }
        }
        self.response = requests.put(SHEERTY_PUT_ENDPOINT, json=data, headers=self.header)
