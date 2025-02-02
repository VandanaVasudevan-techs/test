from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get('https://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Vandana")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Vasudevan")

email = driver.find_element(By.NAME, value="email")
email.send_keys("vandanavasudevan@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()

time.sleep(20)
driver.quit()