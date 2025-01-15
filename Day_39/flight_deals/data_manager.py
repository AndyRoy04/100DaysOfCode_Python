import requests
from pprint import pprint


ENDPOINT_LOG = '173c8e16ea33c53ee4be48c33afaa04c'
SHEERTY_GET_ENPOINT = f'https://api.sheety.co/{ENDPOINT_LOG}/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = SHEERTY_GET_ENPOINT

    def get_data(self):
        self.response = requests.get(self.sheety_url)
        self.data = self.response.json()
        self.prices = self.data['prices']
        # pprint(self.prices)
        return self.prices

    def update_data(self, row_id):
        SHEERTY_PUT_ENDPOINT = f"{SHEERTY_GET_ENPOINT}/{row_id}"
        data = {
            "price": {
                "iataCode": 'TESTING',
            }
        }
        self.response = requests.put(SHEERTY_PUT_ENDPOINT, json=data)
