from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_place = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li a")
events = {}
for n in range(len(event_time)):
    events = {
        "time": event_time[n].text,
        "place": event_place[n].text
    }
    print(events)