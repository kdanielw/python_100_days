from bs4 import BeautifulSoup
import requests
from pprint import pprint
import smtplib
from dotenv import load_dotenv
import os
import json

def add_product():
    
    new_product = {
        "url": input("URL: "),
        "target_price": float(input("Target price: ")),
    }
    product_list = {
        new_product["url"]: new_product,
    }

    try:
        with open("selected_products.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("selected_products.json", mode="w") as file:
            json.dump(product_list, file, indent=4)
    else:        
        data.update(product_list)
        with open("selected_products.json", mode="w") as file:
            json.dump(data, file, indent=4)
    finally:
        pass

def send_email_alert(product_to_buy):
    load_dotenv()
    MY_EMAIL = (os.getenv('MY_EMAIL'))
    GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))
    message = f"{product_to_buy["name"]} is now R$ {product_to_buy["price"]}, below your target price of R$ {product_to_buy["target_price"]}.\n{product_to_buy["url"]}"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Product Below the Target Price!\n\n{message}"
        )

def check_product(product):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Dnt": "1",
        "Priority": "u=0, i",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    }
    
    response = requests.get(url=product["url"], headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    price_decimal = soup.select_one(".a-price-decimal").get_text()
    price_whole = int(soup.select_one(".a-price-whole").get_text().replace(price_decimal,""))
    price_fraction = int(soup.select_one(".a-price-fraction").get_text())
    product_name = soup.select_one("#productTitle").get_text()
    price = price_whole + price_fraction / 100

    product_to_buy = {
        "url": product["url"],
        "target_price": product["target_price"],
        "price": price,
        "name": product_name,
    }

    pprint(product_to_buy)

    if price <= product_to_buy["target_price"]:
        send_email_alert(product_to_buy)

continue_loop = True
while continue_loop == True:
    action = int(input("AMAZON PRICE TRACKER\n1 - Add product\n2 - Check prices\n\nType the number: "))

    if action == 1:
        add_product()
    elif action == 2:
        try:
            with open("selected_products.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Empty List. Please, add a product.")
            add_product()
        else:
            for key in data:
                check_product(data[key])
    elif action == 0:
        continue_loop = False
    
    print("\n\n\n\n\n\n\n\n")