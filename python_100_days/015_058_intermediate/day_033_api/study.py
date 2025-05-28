import requests
from datetime import datetime
import time
import smtplib
from dotenv import load_dotenv
import os

MY_LAT = -10.1848531
MY_LONG = -48.3325364

def can_see_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3
    time_now = datetime.now()

    if time_now.hour > sunset or time_now.hour < sunrise:
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True
    return False

def send_email():
    load_dotenv()
    MY_EMAIL = (os.getenv('MY_EMAIL'))
    GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look Up!\n\nThe ISS is above you"
        )

while True:
    if can_see_iss():
        send_email()
    time.sleep(30 * 1000)
