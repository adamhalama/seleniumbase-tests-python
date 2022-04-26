from seleniumbase import BaseCase


class HomePage(BaseCase):

    logo_icon = ".custom-logo-link"
    get_started = "#get-started"
    heading_text = "h1"
    copyright_text = ".tg-site-footer-section-1"

    menu_links = "li[id*=menu-item]"
    # menu_links = "//*[starts-with(@id, 'menu-item')]"

    username = "testuser5532"
    password = "Sa9DAKicbB6UtJg"

    # wrong password
    # password = "kosekeasda"

    def open_home_page(self):
        url = "https://practice.automationbro.com/"
        self.open(url)

    def logIn(self):
        url = "https://practice.automationbro.com/my-account/"
        self.open(url)
        self.add_text("#username", self.username)
        self.add_text("#password", self.password)
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

    def logOut(self):
        url = "https://practice.automationbro.com/my-account/"
        self.open(url)
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")

