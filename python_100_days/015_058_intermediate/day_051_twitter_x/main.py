from selenium import webdriver
from selenium.webdriver.common.by import By  # Used for searches
import time

PROMISED_DOWN = 500
PROMISED_UP = 50
INTERNET_PROVIDER = "Internet Provider"

class InternetSpeedBot:
    def __init__(self, driver_path):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome()
        self.driver.get(url=driver_path)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        start_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_button.click()
        time.sleep(60)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)


    def send_message(self):
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            print(f"Hey {INTERNET_PROVIDER}, why is my internet speed {self.down}mb download / {self.up}mb upload when I pay for {PROMISED_DOWN}mb download / {PROMISED_UP}mb upload?")

path = "https://www.speedtest.net/"
bot = InternetSpeedBot(path)
bot.get_internet_speed()
bot.send_message()
