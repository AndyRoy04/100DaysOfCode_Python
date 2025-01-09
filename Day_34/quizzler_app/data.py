import requests

response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
response.raise_for_status()
json_data_format = response.json()
questions = json_data_format['results']

# Extracting the required information from the JSON data
question_data = questions
