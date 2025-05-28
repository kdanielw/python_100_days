import pandas
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

##################### Extra Hard Starting Project ######################

def send_congrats(person):
    load_dotenv()
    MY_EMAIL = (os.getenv('MY_EMAIL'))
    GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))

    letter_number = random.randint(1, 3)
    letter_path = f"letter_templates/letter_{letter_number}.txt"
    with open(letter_path) as file:
        message = file.read().replace("[NAME]", person["name"])
    
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["name"],
            msg=f"Subject:Happy Birthday!!!\n\n{message}"
        )

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
persons = data.to_dict("records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month
for person in persons:
    if current_day == person["day"] and current_month == person["month"]:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        send_congrats(person)
    











