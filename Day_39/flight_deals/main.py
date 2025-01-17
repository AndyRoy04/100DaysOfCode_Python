from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()
data_manager = DataManager()

sheet_data = data_manager.get_data()
users_emails = data_manager.get_customer_emails()


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row['city'])
        data_manager.update_data(row['id'],
                                 row["iataCode"]
                                 )

    print(f"Getting flights for {row['city']}...")
    current_price, stops, carriers = flight_data.find_cheapest_flight(row["iataCode"],
                                                                      flight_search._get_new_token(),
                                                                      row['city']
                                                                      )

    # Uncomment to send message through whatsapp
    notification_manager.send_message(current_price,
                                      row['lowestPrice'],
                                      row["iataCode"],
                                      flight_data.tomorrow,
                                      flight_data.return_date,
                                      stops,
                                      carriers,
                                      )

    notification_manager.send_email(users_emails,
                                    current_price,
                                    row['lowestPrice'],
                                    row["iataCode"],
                                    flight_data.tomorrow,
                                    flight_data.return_date,
                                    stops,
                                    carriers
                                    )
