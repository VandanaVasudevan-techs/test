from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://www.python.org/")
#to click on buttons
# element = driver.find_element(By.XPATH, value='//*[@id="touchnav-wrapper"]/header/div/div[1]/a')
# element.click()
#to type something and click enter
element1 = driver.find_element(By.XPATH, value='//*[@id="id-search-field"]')
element1.send_keys("about", Keys.ENTER)
time.sleep(1)
