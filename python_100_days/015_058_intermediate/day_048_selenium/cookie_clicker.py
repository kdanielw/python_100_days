from selenium import webdriver
from selenium.webdriver.common.by import By  # Used for searches
import time

def buy():
    best_buy = driver.find_elements(By.CSS_SELECTOR, value=".storeSection .enabled")[-1]
    best_buy.click()

def clicker(big_cookie):
    click_start = time.time()
    click_duration = 10
    while time.time() - click_start < click_duration:
        big_cookie.click()    

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)  # Option to keep Chrome open 
driver = webdriver.Chrome(options=options)

driver.get(url="https://ozh.github.io/cookieclicker/")

time.sleep(2)
language = driver.find_element(By.ID, value="langSelect-PT-BR")
language.click()
time.sleep(2)

big_cookie = driver.find_element(By.ID, value="bigCookie")

game_start = time.time()
game_duration = 5 * (60)

while time.time() - game_start < game_duration:
    clicker(big_cookie)
    buy()

cookies = driver.find_element(By.ID, value="cookiesPerSecond")
print(f"After {game_duration/60} min. Cookies {cookies.text}.")

driver.quit()