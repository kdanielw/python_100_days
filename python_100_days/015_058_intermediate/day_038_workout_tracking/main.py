import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
MY_INFOS = (os.getenv('MY_INFOS'))
NUTRITIONIX_API_KEY = (os.getenv('NUTRITIONIX_API_KEY'))
NUTRITIONIX_ID = (os.getenv('NUTRITIONIX_ID'))
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/"
NUTRITIONIX_ENDPOINT_EXERCISE = f"{NUTRITIONIX_ENDPOINT}v2/natural/exercise"

SHEETY_ENDPONT = (os.getenv('SHEETY_ENDPONT'))
SHEETY_AUTHORIZATION = (os.getenv('SHEETY_AUTHORIZATION'))


MY_INFOS = {
    "weight_kg": (os.getenv('WEIGHT')),
    "height_cm": (os.getenv('HEIGHT')),
    "age": (os.getenv('AGE')),
    "gender": (os.getenv('GENDER')),
}

def post_request(ENDPOINT, JSON, HEADERS):
    response = requests.post(url=ENDPOINT, json=JSON, headers=HEADERS)
    data = response.json()
    return data

nutriotionix_params = MY_INFOS
nutriotionix_params["query"] = input("Tell me which exercise you did: ")
response = requests.post(url=NUTRITIONIX_ENDPOINT_EXERCISE, json=nutriotionix_params, headers=NUTRITIONIX_HEADERS)
nutriotionix_data = response.json()

SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTHORIZATION,
}

today = datetime.now()
for exercise in nutriotionix_data["exercises"]:
    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }        
    }
    sheety_data = requests.post(url=SHEETY_ENDPONT, json=sheety_params, headers=SHEETY_HEADERS)
