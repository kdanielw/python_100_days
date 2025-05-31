import requests
import requests_cache
from dotenv import load_dotenv
import os
import smtplib

VARIATION_LIMIT = 1/100
STOCK = "AMD"
COMPANY_NAME = "AMD"
email_title = ""
email_text = ""

load_dotenv()
MY_EMAIL = (os.getenv('MY_EMAIL'))
GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))


def get_request(NAME, ENDPOINT, PARAMS):
    stock_session = requests_cache.CachedSession(f"{NAME}_cache", expire_after=3600)
    response = stock_session.get(url=ENDPOINT, params=PARAMS)
    data = response.json()
    return data

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWS_APIKEY = (os.getenv('NEWS_APIKEY'))
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "apiKey": NEWS_APIKEY,
    "q": f"\"{COMPANY_NAME}\"",
    "searchIn": "title",    
    "language": "en",
    "pageSize": 10,
}

def get_news():
    global email_text

    data_news= get_request("newsapi", NEWS_ENDPOINT, NEWS_PARAMS)
    data_news["articles"]

    count_news = 1
    for news in data_news["articles"]:
        try:
            if len(news["description"]) > 10 and count_news <= 3 :
                email_text += f"Headline: {news["title"]}\n"
                email_text += f"Brief:  {news["description"]}\n\n"
        except:
            pass
        else:
            count_news += 1
    send_email()


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_email():
    global MY_EMAIL
    global GOOGLE_SMTP_PASSWORD
    global email_text
    global email_title

    print(email_title)
    print(email_text)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:{email_title.encode("utf-8")}\n\n{email_text.encode("utf-8")}"
        )

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHA_VANTAGE_APIKEY = (os.getenv('ALPHA_VANTAGE_APIKEY'))
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "outputsize": "compact",
    "apikey": ALPHA_VANTAGE_APIKEY,
}

data_stock = get_request("alphavantage", ALPHA_VANTAGE_ENDPOINT,ALPHA_VANTAGE_PARAMS)

yesterday = {}
before_yesterday = {}
count_days = 1

for key in data_stock["Time Series (Daily)"]:
    if count_days == 1:
        yesterday = data_stock["Time Series (Daily)"][key]
        count_days += 1
    elif count_days == 2:
        before_yesterday = data_stock["Time Series (Daily)"][key]
        break

increase_decrease = round((float(yesterday["4. close"]) - float(before_yesterday["4. close"])) / float(before_yesterday["4. close"]), 4)
increase_decrease_percent = increase_decrease * 100

if increase_decrease >= VARIATION_LIMIT:
    email_title += f"{STOCK}: 🔺 {increase_decrease_percent}%"
    get_news()
elif increase_decrease <= -VARIATION_LIMIT:
    email_title += f"{STOCK}: 🔻 {increase_decrease_percent}%"
    get_news()
