from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys


class CartTest(CartPage):

    def setUp(self):
        super().setUp()

        # open page
        self.open("https://practice.automationbro.com/shop")


    def test_add_to_cart(self):
        pass
        # add item to cart
        self.click(self.converse_add_to_cart_btn)

        # assert product is added to cart
        self.assert_text("1", self.cart_count_text)

        # open cart page
        self.open_cart_page()

        # get current subtotal
        original_subtotal = self.get_text(self.subtotal_text)
        print(original_subtotal)

        # change cart quantity
        self.set_value(self.product_quantity_input, '2')
        self.send_keys(self.product_quantity_input, Keys.RETURN)


        # confirm change  with a click
        self.click(self.update_cart_btn)

        # wait a few seconds
        # bad practice
        # self.wait(4)

        # wait for loading to be completed
        self.wait_for_element_visible(self.loading_overlay)
        self.wait_for_element_not_visible(self.loading_overlay)


        # wait for the text to change to specified
        # self.wait_for_text("$300.00", self.subtotal_text)

        # assert subtotal to be different from original subtotal
        updated_subtotal = self.get_text(self.subtotal_text)
        print(updated_subtotal)

        self.assertNotEqual(original_subtotal, updated_subtotal)

