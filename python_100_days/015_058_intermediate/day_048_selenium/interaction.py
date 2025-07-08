from selenium import webdriver
from selenium.webdriver.common.by import By  # Used for searches
from selenium.webdriver.common.keys import Keys
 
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)  # Option to keep Chrome open 
driver = webdriver.Chrome(options=options)

# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# total_articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="article count documentation")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Isagi")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Yoichi")

email = driver.find_element(By.NAME, value="email")
email.send_keys("demonking@bluelock.com")

sing_up_button = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
sing_up_button.click()


# driver.quit()