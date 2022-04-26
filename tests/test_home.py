from seleniumbase import BaseCase
import json

from page_objects.home_page import HomePage


class HomeTest(HomePage):
    def setUp(self):
        # at start
        super().setUp()

        print("\nrunning before each")

        # LOGIN
        HomePage.logIn(self)

        # open homepage
        HomePage.open_home_page(self)

        
    def tearDown(self):
        print("running after each")

        # LOGOUT c
        HomePage.logOut(self)

        # at the end
        super().tearDown()




    def test_home_page(self):
        # assert page title
        title = "Practice E-Commerce Site – Automation Bro"
        self.assert_title(title)

        # assert logo
        self.assert_element(HomePage.logo_icon)

        # click on the get started button and assert the url
        getStartedUrlExpected = "https://practice.automationbro.com/#get-started"

        self.click(HomePage.get_started)
        getStartedUrl = self.get_current_url()

        self.assert_equal(getStartedUrl, getStartedUrlExpected)
        self.assert_true(HomePage.get_started in getStartedUrl)

        # get the text of the header and
        h1Text = "Think different. Make different."
        self.assert_text(h1Text, HomePage.heading_text)

        # assert the copyright text
        self.scroll_to_bottom()
        copyrightText = "Copyright © 2020 Automation Bro"
        self.assert_text(copyrightText, HomePage.copyright_text)

        print(self.get_text(HomePage.copyright_text))

    def test_menu_links(self):
        expectedLinks = json.loads(open("./tests/expectedLinks.json").read())
        print(expectedLinks)

        # li[id*=menu-item]

        # find menu link elements
        # elements = "//*[starts-with(@id, 'menu-item')]"
        menuLinks = self.find_elements(HomePage.menu_links)

        # loop trough our menu links
        for idx, link in enumerate(menuLinks):
            # print(idx, link.text)
            self.assert_equal(expectedLinks[idx], link.text)
