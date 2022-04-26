from page_objects.contact_page import ContactPage


class ContactTest(ContactPage):
    def test_contact_page(self):
        # open page
        ContactPage.open_contact_page(self)

        # scroll to empty form and screenshot
        self.scroll_to(self.form_tag)
        self.save_screenshot("empty_contact_form", "custom_screenshots")

        # fill in all the fields
        # name
        self.send_keys(ContactPage.name_input, "Test Name")
        # email
        self.send_keys(ContactPage.email_input, "test@gmail.com")
        # phone
        self.send_keys(ContactPage.phone_input, "0123456789")
        # message
        self.send_keys(ContactPage.message_input, "Some message")

        # filled form and screenshot
        self.scroll_to(self.form_tag)
        self.save_screenshot("filled_contact_form", "custom_screenshots")

        # click the submit button
        self.click(ContactPage.submit_button)

        # verify submit message
        self.assert_text(ContactPage.submit_message_text, ContactPage.submit_message_tag)
