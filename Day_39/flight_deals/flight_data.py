import requests
import os
from dotenv import load_dotenv
import datetime

TOMORROW_DATE = datetime.date.today() + datetime.timedelta(days=1)      # Provides us with tomorrow's date
FUTURE_DATE = datetime.date.today() + datetime.timedelta(days=6*30)

load_dotenv()


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET_KEY")
        self.price = 0
        self.depature_city_code = 'IAD'
        self.tomorrow = TOMORROW_DATE
        self.return_date = FUTURE_DATE
        
    def find_cheapest_flight(self, city_code, token, city_name):
        url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        
        parameters = {
            "originLocationCode": self.depature_city_code,
            "destinationLocationCode": city_code,
            "departureDate": TOMORROW_DATE,
            "returnDate": FUTURE_DATE,
            "nonStop": "false",     # when nonstop is true, flights are expensive and rare
            "currencyCode": "USD",
            # "maxPrice": price,
            "adults": 1,
        }
        
        header = {
            "Authorization": f"Bearer {token}"
        }
        
        response = requests.get(url, params=parameters, headers=header)
        response.raise_for_status()
        
        data = response.json()
        
        # # Check if no flights are found for the given city
        if data['data'] == []:
            print(f"No flight for {city_name} found\n{city_name}: N/A")
        else:
            self.price = data['data'][0]['price']['grandTotal']
            print(f"{city_name}: ${self.price}")
            return self.price
    