import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
PIXELA_TOKEN = (os.getenv('PIXELA_TOKEN'))
PIXELA_USERNAME = (os.getenv('PIXELA_USERNAME'))
MY_EMAIL = (os.getenv('MY_EMAIL'))
GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create your user account
# response = requests.post(url=PIXELA_USER_ENDPOINT, json=PIXELA_USER_PARAMS)
# print(response.text)

# Create a graph definition
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXELA_GRAPH_PARAMS = {
    "id": "kindle1",
    "name": "Kindle's Reanding Graph",
    "unit": "pages",
    "type": "int",
    "color": "kuro",
}

PIXELA_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=PIXELA_GRAPH_PARAMS, headers=PIXELA_HEADERS)
# print(response.text)

# Post value to the graph -----------------------------------------------------
today = datetime.now()

PIXELA_INPUT_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRAPH_PARAMS['id']}"
PIXELA_INPUT_PARAMS = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did I read today? "),
}

print(PIXELA_INPUT_PARAMS)
response = requests.post(url=PIXELA_INPUT_ENDPOINT, json=PIXELA_INPUT_PARAMS, headers=PIXELA_HEADERS)
print(response.text)

# Update value to the graph -----------------------------------------------------
day_to_update = "20250531"
PIXELA_UPDATE_ENDPOINT = f"{PIXELA_INPUT_ENDPOINT}/{day_to_update}"
PIXELA_UPDATE_PARAMS = {
    "quantity": "7",
}
# response = requests.put(url=PIXELA_UPDATE_ENDPOINT, json=PIXELA_UPDATE_PARAMS, headers=PIXELA_HEADERS)

# Dalete value to the graph -----------------------------------------------------
# response = requests.delete(url=PIXELA_UPDATE_ENDPOINT, headers=PIXELA_HEADERS)
# print(response.text)
