from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class EcommercePage:

    PRODUCTS_TAB = (By.XPATH, "//a[@href='/products']")
    SEARCH_PRODUCT = (By.ID, "search_product")
    SEARCH_ICON = (By.CSS_SELECTOR, ".fa-search")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".productinfo p")
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart")


    def __init__(self, driver):
        self.driver = driver

    def go_to_products_tab(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.PRODUCTS_TAB)).click()

    def search_products(self,product_name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.SEARCH_PRODUCT)).send_keys(product_name)
        wait.until(EC.element_to_be_clickable(self.SEARCH_ICON)).click()

    def add_to_cart(self,product_name):
        products_result = self.driver.find_elements(self.PRODUCT_ITEMS)
        for product in products_result:
            if product.text == product_name:
                product.click()
                break










