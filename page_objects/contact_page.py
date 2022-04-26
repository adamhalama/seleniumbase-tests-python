from seleniumbase import BaseCase


class ContactPage(BaseCase):
    name_input = ".contact-name input"
    email_input = ".contact-email input"
    phone_input = ".contact-phone input"
    message_input = ".contact-message textarea"

    submit_button = "#evf-submit-277"

    form_tag = "#evf-form-277"

    submit_message_text = "Thanks for contacting us! We will be in touch with you shortly"

    # to fail
    submit_message_text = "Thanks for us! We will be in touch with you shortly"

    # submit_message_tag = "div[role=alert]"

    def open_contact_page(self):
        url = "https://practice.automationbro.com/contact"
        self.open(url)
