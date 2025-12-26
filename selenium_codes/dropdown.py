import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.CSS_SELECTOR, '#autosuggest').send_keys("IND")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        time.sleep(5) 
        break


