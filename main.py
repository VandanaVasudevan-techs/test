from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://www.amazon.in/Noise-Launched-Wireless-Playtime-Instacharge/dp/B0CQJZD55X/ref=sr_1_8?_encoding=UTF8&content-id=amzn1.sym.82b20790-8877-4d70-8f73-9d8246e460aa&dib=eyJ2IjoiMSJ9.ywhx7vPzGx0BrZMAiYuhTjEe7FUM7ua-xWqDZmdm_U_eggvWktcas85SNa7BcUzEVx_rU-dYhXFVllOShkdtQ6q_xPfJ1kTOyR5ZT2t-5W3qUmuoqVTPNU7Ssl23FG0zY2_CC5cBJhfSA0KI6n36_PfitKW-xZ9C37sd1aRclqmYMmXwwzZXVRVkpaD9A-mdsjvsHTXv0Q9KiGx19z2aiIlLEQA-AeYkLKVFqu6E2DyLjBwVT_gVzv3BIs2iOLaxEi1A6ikRdckIoACuV4Dsk2CHQvlhvmMp4gZjTwjrHfFrWl5NNEuzktSGWRJnWaBHSIVKckI3_vjSCOJ2H19y-Ru44FeO78vHb_KgwWT2eZY.MbzZw0WNDFCoZjgh3ML_pNMpvo8zrPqycO9_Y87W898&dib_tag=se&keywords=noise&pd_rd_r=78c94f60-38ca-46bf-bb94-c012bc2dc4bc&pd_rd_w=4YH7P&pd_rd_wg=DRwbl&qid=1738388874&refinements=p_n_condition-type%3A8609960031%2Cp_36%3A-200000&s=electronics&sr=1-8&th=1")
# element = driver.find_element(By.CLASS_NAME, "a-size-medium-plus a-spacing-none a-color-base a-text-bold")
# print(element.text)

# time.sleep(20)
# # driver.quit()

# driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")
element = driver.find_element(By.CLASS_NAME, "a-price-whole").text
print(f"The price is {element}")
time.sleep(10)
driver.quit()