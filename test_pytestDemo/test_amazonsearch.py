from pages.amazon import AmazonPage


class TestAmazonPage:

    def test_amazon_search(self,driver_sel):
        driver_sel.maximize_window()
        driver_sel.get("https://www.amazon.in")
        assert "Amazon" in driver_sel.title

        amazon = AmazonPage(driver_sel)

        amazon.amazon_search("laptop")

        assert "laptop" in driver_sel.title.lower()

        name,price = amazon.search_product_mouse("wireless mouse")
        print(name,price)


        assert "wireless mouse" in driver_sel.title.lower()





