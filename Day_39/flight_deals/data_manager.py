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
        self.sheety_end_point = f'https://api.sheety.co/{self.end_log}/flightDeals/prices'

    def get_data(self):
        self.response = requests.get(self.sheety_end_point, headers=self.header)
        self.data = self.response.json()
        self.prices = self.data['prices']
        return self.prices

    def update_data(self, row_id, iata_code):
        SHEERTY_PUT_ENDPOINT = f"{self.sheety_end_point}/{row_id}"
        data = {
            "price": {
                "iataCode": iata_code,
            }
        }
        self.response = requests.put(SHEERTY_PUT_ENDPOINT, json=data, headers=self.header)
