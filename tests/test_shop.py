from selenium.common.exceptions import NoSuchElementException

from page_objects.shop_page import ShopPage


class ShopTest(ShopPage):

    def test_search_product(self):

        # open page
        self.open_shop_page()

        # search for product
        self.send_keys(self.search_input, "Toys")

        # click search button
        self.click(self.search_btn)

        # assert product image
        try:
            self.assert_element(self.product_img)
        except NoSuchElementException:
            self.assert_text(self.no_products_text, self.no_products_tag)



