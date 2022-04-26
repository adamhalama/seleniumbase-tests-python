from seleniumbase import BaseCase


class ShopPage(BaseCase):
    search_input = "#woocommerce-product-search-field-0"
    search_btn = "button[value='Search']"
    product_img = ".woocommerce-product-gallery__image"
    no_products_tag = ".woocommerce-info"

    no_products_text = "No products were found matching your selection."

    def open_shop_page(self):
        self.open("https://practice.automationbro.com/shop")
