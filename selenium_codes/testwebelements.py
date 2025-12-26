from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/ASUS/Desktop/practice.html")

driver.find_element(By.ID, 'username').send_keys("Test")

driver.find_element(By.CSS_SELECTOR, 'input[type= "password"]').send_keys("12345678")

driver.find_element(By.TAG_NAME, 'input').click()

driver.find_element(By.CSS_SELECTOR, '#male').click()

dropdown_element = (driver.find_element(By.CSS_SELECTOR, '#country'))
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("USA")

# driver.find_element(By.ID, "googleLink").click()
#
#
# # google_link = driver.find_element(By.LINK_TEXT, "Visit Google")
# # google_link.click()


table = driver.find_element(By.ID,'dataTable')
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    cells = row.find_elements(By.XPATH, './/th | .//td')
    row_data = []
    for cell in cells:
        text = cell.text
        row_data.append(text)
    print(row_data)



##time.sleep(10)

