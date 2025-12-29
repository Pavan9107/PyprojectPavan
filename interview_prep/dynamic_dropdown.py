from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()

driver.find_element(By.ID, 'autosuggest').send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'li.ui-menu-item')))

options = driver.find_elements(By.CSS_SELECTOR,'li.ui-menu-item')

for option in options:
    if option.text == 'India':
        option.click()
        break




