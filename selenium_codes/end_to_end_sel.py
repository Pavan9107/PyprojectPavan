import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.LINK_TEXT, 'Shop').click()

product_list = [product.text for product in driver.find_elements(By.CSS_SELECTOR, "div[class='col-lg-9'] .row h4")]


for product in product_list:
    if product == "iphone X":
        driver.find_element(By.XPATH, '//button[@class = "btn btn-info"]').click()
        driver.find_element(By.CSS_SELECTOR,'.nav-link.btn.btn-primary').click()
        driver.find_element(By.CSS_SELECTOR, '.btn.btn-success').click()
        driver.find_element(By.ID, 'country').send_keys("ind")
        time.sleep(10)
        drop_down = driver.find_elements(By.CSS_SELECTOR, 'div[class="suggestions"] li')
        drop_down[0].click()
        #driver.find_element(By.ID, 'checkbox2').click()
        driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
        success_message = driver.find_element(By.CSS_SELECTOR, "div.alert-success")
        print(success_message.text)















