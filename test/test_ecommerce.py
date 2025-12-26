from pages.home_page import EcommercePage


def test_ecommerce(driver_setup):
    driver = driver_setup
    e_page = EcommercePage(driver)  # pass fixture
    e_page.go_to_products_tab()
    e_page.search_products("Tshirt")
    e_page.add_to_cart("Men Tshirt")

