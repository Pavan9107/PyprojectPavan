from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonPage:
    search_bar = "//input[@id='twotabsearchtextbox']"
    search_mouse = "//span[contains(text(),'Logitech M196 Bluetooth Wireless Mouse, Compa…')]"
    mouse_price = "(//span[@class='a-offscreen'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def amazon_search(self, user_input):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_bar)))
        search_box.click()
        search_box.send_keys(user_input + Keys.RETURN)

    def search_product_mouse(self, user_input):
        wait = WebDriverWait(self.driver, 10)
        search_mouse_results = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_bar)))
        search_mouse_results.click()
        search_mouse_results.send_keys(user_input + Keys.RETURN)
        mouse_name = wait.until(EC.visibility_of_element_located((By.XPATH,self.search_mouse))).text
        mouse_price_rec = self.driver.find_element(By.XPATH, self.mouse_price).text
        return mouse_name, mouse_price_rec


