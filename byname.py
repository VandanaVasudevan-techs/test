from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
element = driver.find_element(By.NAME, value="q")
element2 = driver.find_element(By.CLASS_NAME, value="slide-copy")
print(element.get_attribute("placeholder"))# to get the placeholder of an element
print(element.tag_name) # to get the tagname
print(element2.text)
element3 = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(element3.text)
element4 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[1]/div[1]/p[2]/a')
print(element4.text)