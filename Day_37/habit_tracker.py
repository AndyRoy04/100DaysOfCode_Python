import requests
import datetime as dt

USER_NAME = "USER NAME FROM PIXELA"
TOKEN = "TOKEN FROM PIXELA"
GRAPH_NAME = "graphone404"
DATE = dt.datetime.now().strftime("%Y%m%d")     # this helps convert the date into a desired format


# Setting up the Pixela API endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# Setting up a user account on Pixela
parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=parameters)
# print(response.status_code)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_header = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": GRAPH_NAME,
    "name": "FOREX Researches/Trading",
    "unit": "pages/executions",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(graph_endpoint, json=graph_params, headers=graph_header)   # always include the Header
# print(response.status_code)
# print(response.text)

pixel_post_endpoint = f"{graph_endpoint}/{GRAPH_NAME}"
pixel_params = {
    "date": '20241013',
    "quantity": '10',
}

response = requests.post(pixel_post_endpoint, json=pixel_params, headers=graph_header) # always include the Header
print(response.status_code)
print(response.text)

put_endpoint = f"{pixel_post_endpoint}/20250103" 
put_params = {
    "quantity": '3',
}

# response = requests.put(put_endpoint, json=put_params, headers=graph_header) # always include the Header
# print(response.status_code)
# print(response.text)

# delete_endpoint = f"{pixel_post_endpoint}/20250103" 
# response = requests.delete(delete_endpoint, headers=graph_header)
# print(response.text)
