from selenium import webdriver
from selenium.webdriver.common.by import By  # Used for searches
from pprint import pprint
 
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)  # Option to keep Chrome open 
driver = webdriver.Chrome(options=options)
 
# driver.get(url="https://www.amazon.com.br/Camisa-1-Flamengo-Tamanho-G/dp/B0DDHGBR3Q/?_encoding=UTF8")
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is R$ {price_whole},{price_fraction}")

# driver.get(url="https://www.python.org")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget p a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

driver.get(url="https://www.python.org")
events_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div .menu li time")
events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div .menu li a")

events = {i: {"time": events_date[i].text, "name": events_name[i].text} for i in range(len(events_date))}
pprint(events)





driver.quit() # all tabs
# driver.close() # actual tab