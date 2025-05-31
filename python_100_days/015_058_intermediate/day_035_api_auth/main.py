import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
MY_EMAIL = (os.getenv('MY_EMAIL'))
GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))
WEATHER_API_KEY = (os.getenv('API_KEY'))

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_PARAMS = {
    "appid" : WEATHER_API_KEY,
    "lon": -75.627769,
    "lat": 2.19593,
    "cnt": 4,
    "units": "metric",
}
LON = -48.360279
LAT = -10.21278

def get_weather_data():
    response = requests.get(url=WEATHER_ENDPOINT, params=WEATHER_API_PARAMS)
    response.raise_for_status()
    weather_data = response.json()

    for forecast in weather_data["list"]:
        for weather in forecast["weather"]:
            print(weather["id"])
            if weather["id"] < 700:
                return True
    return False

def bring_umbrella():
    if get_weather_data():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Bring an Umbrella!!!\n\nIt's going to rain today. Remember to bring an umbrella."
        )

bring_umbrella()
