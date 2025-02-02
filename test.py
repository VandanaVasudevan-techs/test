from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Your WhatsApp number and message
target_number = "9746655433"  # Change this to the recipient's WhatsApp number
message = "Hello! This is an automated message from Selenium."

# Set up Selenium WebDriver (Make sure ChromeDriver is installed)
driver = webdriver.Chrome()  # Change to your WebDriver if needed

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Scan the QR code and press Enter to continue...")  # Wait for manual login

# Construct WhatsApp Web URL to directly open the chat
chat_url = f"https://web.whatsapp.com/send?phone={target_number}&text={message}"
driver.get(chat_url)

time.sleep(5)  # Wait for the page to load

# Locate the send button and click it
send_button_xpath = "//button[@data-testid='send']"
send_button = driver.find_element(By.XPATH, send_button_xpath)
send_button.click()

print("Message sent successfully!")

# Close the browser after some time
time.sleep(5)
driver.quit()
