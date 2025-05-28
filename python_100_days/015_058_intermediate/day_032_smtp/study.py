import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import pandas
import random

DICT_WEEKDAYS = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

def motivational_quote_weekday(weekday):
    global DICT_WEEKDAYS

    if DICT_WEEKDAYS[weekday] == dt.datetime.now().weekday():
        pick_quote(weekday)

def pick_quote(weekday):
    with open("quotes.txt", mode="r") as file:
        quotes = file.read().splitlines()
    pick_quote = random.choice(quotes)
    
    send_email(weekday, pick_quote)

def send_email(weekday, message):
    load_dotenv()
    MY_EMAIL = (os.getenv('MY_EMAIL'))
    GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))
    RECEIVER = (os.getenv('RECEIVER'))

    subject = f"Good {weekday.capitalize()}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER,
                msg=f"Subject:{subject}\n\n{message}"
            )

motivational_quote_weekday("tuesday")
