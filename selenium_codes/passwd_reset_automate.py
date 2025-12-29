import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, 'input[type = "email"]').send_keys("123@gmail.com")
driver.find_element(By.CSS_SELECTOR, '#userPassword').send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('12345678')
driver.find_element(By.CSS_SELECTOR, '.form-control').click()
driver.find_element(By.CSS_SELECTOR,  'button[type="submit"]').click()
time.sleep(10)