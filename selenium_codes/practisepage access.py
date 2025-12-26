import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.switch_to.frame()

driver.get("https://rahulshettyacademy.com/practice-project")
driver.find_element(By.ID, 'name' ).send_keys('Pavan')
driver.find_element(By.CSS_SELECTOR, 'input[id="email"]').send_keys('2019pavan@gmail.com')
#driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR, '#agreeTerms').click()  #[#id is shortcut valid CSS selector]
#.class name is also another valid CSS selector
#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").submit()
# Keep browser open until you press Enter in terminal
input("Press ENTER to close the browser...")
driver.quit()


#time.sleep(20)
