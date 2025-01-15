#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_data()
# pprint(sheet_data)

for row in sheet_data:
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row['city'])
    data_manager.update_data(row['id'])

# pprint(sheet_data)

# for row in sheet_data:
