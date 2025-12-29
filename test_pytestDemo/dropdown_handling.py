import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
wait = WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.ID, 'dropdown-class-example')))

dropdown = driver.find_element(By.ID, 'dropdown-class-example')
select = Select(dropdown)

select.select_by_visible_text('Option2')

assert select.first_selected_option.text == 'Option2'

