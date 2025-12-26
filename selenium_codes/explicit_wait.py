from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
input("Browser is open — inspect the element, then press Enter to continue...")
print("Continuing script...")
try:
    popup = WebDriverWait(driver,10).until(element_to_be_clickable((By.CSS_SELECTOR, "button.a-button-text[alt='Continue shopping']")))
    popup.click()

except TimeoutException:
    print("Timed out.")

search_box = WebDriverWait(driver, 10).until(presence_of_element_located((By.ID, 'twotabsearchtextbox')))
search_box.send_keys("laptop")

# wait = WebDriverWait(driver, 10)
# wait.until(element_to_be_clickable((By.ID, 'nav-search-submit-button')))


products = driver.find_elements(By.CSS_SELECTOR, 'div.left-pane-results-container div[role="row"]')

while True:
    try:
        products = driver.find_elements(By.CSS_SELECTOR, 'div.left-pane-results-container div[role="row"]')
        for product in products:
            if "laptop table stand" in product.text.lower():
                product.click()
                print("Clicked on laptop table stand!")
        break
    except StaleElementReferenceException:
        print("Stale element detected. Retrying...")
