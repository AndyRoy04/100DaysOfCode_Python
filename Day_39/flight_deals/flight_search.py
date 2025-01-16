import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET_KEY")
        self._token = self._get_new_token()
    def get_iata_code(self, city):
        """This function returns the IATA code from a certain city"""
        parameters = {
            'keyword': city.capitalize(),
        }
        get_header = {
            "Authorization": f"Bearer {self._get_new_token()}"
        }
        get_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        response = requests.get(get_url, params=parameters, headers=get_header)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        else:
            city_code = data["iataCode"]
            return city_code
    
    def _get_new_token(self):
        """This function helps get a new token from Amadeus everytime the code runs"""
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        response.raise_for_status()
        return response.json()['access_token']
            
