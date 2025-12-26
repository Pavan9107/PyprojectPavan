import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")


driver.find_element(By.CLASS_NAME, 'blinkingText').click()



driver.switch_to.window(driver.window_handles[1])
email_element = driver.find_element(By.LINK_TEXT, 'mentor@rahulshettyacademy.com')
email_text = email_element.text
print(email_text)

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.ID, 'username').send_keys(email_text)
time.sleep(10)

driver.find_element(By.ID, 'password').send_keys('12345678')
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
time.sleep(5)