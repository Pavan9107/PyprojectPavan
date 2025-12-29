import time

from selenium import webdriver
#
# webdriver = webdriver.Chrome()
# webdriver.get('http://www.google.com')

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#driver.get('http://www.google.com')
#driver.get('http://www.rahulshettyacademy.com/')
# driver.get('https://rahulshettyacademy.com/angularpractice/')
# driver.find_element(By.NAME, 'email').send_keys('2019pavan@gmail.com')
# driver.find_element(By.ID, "exampleInputPassword1").send_keys('12345678')

driver.get('http://www.rahulshettyacademy.com/practice-project')
driver.find_element(By.ID, 'name').send_keys('Pavan')
driver.find_element(By.XPATH, '//input[@name = "email"]').send_keys('abc@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'button[id="form-submit"').click()

time.sleep(10)
