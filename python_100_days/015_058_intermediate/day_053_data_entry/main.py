from bs4 import BeautifulSoup
import requests
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By  # Used for searches
from selenium.webdriver.common.keys import Keys
import time

FORM_LINK = "https://forms.gle/5kvGVEJTeEmjaUrF9"
ZILLOW_CLONE = "https://appbrewery.github.io/Zillow-Clone/"

def clean_text(text):
    text_list = list(text)
    for i in range(len(text_list) -1, -1, -1):
        if text_list[i] == "\n":
            text_list.pop(i)
    while text_list[0] == " ":
        text_list.pop(0)
    return "".join(text_list)

def data_entry(driver, data):
    global FORM_LINK

    driver.get(url=FORM_LINK)
    time.sleep(1)
    question_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_address.send_keys(f"{data["address"]}")

    question_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_price.send_keys(data["price"])
    
    question_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_link.send_keys(data["link"])

    submit_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_form.click()


reponse = requests.get(ZILLOW_CLONE)
soup = BeautifulSoup(reponse.text, "html.parser")

prices = [price.string.split("/")[0].split("+")[0] for price in
          soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")]

links = [link.get("href") for link in
         soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")]

addresses = [clean_text(address.string) for address in
          soup.find_all("address")]

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)  # Option to keep Chrome open 
driver = webdriver.Chrome(options=options)

for i in range(len(links)):
    data = {
        "address": addresses[i],
        "price": prices[i],
        "link": links[i],
    }
    data_entry(driver, data)
    time.sleep(2)
