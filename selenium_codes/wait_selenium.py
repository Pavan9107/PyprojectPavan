import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

webdriver.implicitly_wait(10)

webdriver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
webdriver.find_element(By.CLASS_NAME, 'search-keyword').send_keys("ber")
time.sleep(4)


products_list = webdriver.find_elements(By.CSS_SELECTOR, '.products div.product')
for product in products_list:
    product.find_element(By.XPATH, './/button[text()="ADD TO CART"]').click()
#time.sleep(5)

webdriver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
#time.sleep(5)

webdriver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()
#time.sleep(5)

amount  = webdriver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(5) p')
print(len(amount))
sum = 0
for value in amount:
    sum += int(value.text)

print(sum)

webdriver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
webdriver.find_element(By.XPATH, '//button[text()="Apply"]').click()
time.sleep(10)
message = webdriver.find_element(By.CLASS_NAME, "promoInfo")

assert "applied" in message.text

amount = int(webdriver.find_element(By.CSS_SELECTOR, '.totAmt').text)
discounted_amount = float(webdriver.find_element(By.CSS_SELECTOR, '.discountAmt').text)

assert discounted_amount < amount

webdriver.find_element(By.XPATH, '//Button[text() = "Place Order"]').click()
#time.sleep(5)

