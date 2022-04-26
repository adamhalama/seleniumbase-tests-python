from seleniumbase import BaseCase


class UploadPage(BaseCase):

    logo_file_path = "./data/logo.jpg"

    upload_file_tag_simple = "#file-upload"
    click_button_tag_simple = "#file-submit"
    uploaded_tag_simple = "h3"
    uploaded_text_simple = "File Uploaded!"

    remove_hidden_class = 'document.getElementById("upfile_1").classList.remove("file_input_hidden")'

    upload_file_tag_hidden = "#upfile_1"
    click_button_tag_hidden = "#upload_1"
    uploaded_tag_hidden = "#wfu_messageblock_header_1_label_1"
    uploaded_text_hidden = "uploaded successfully"


    def open_upload_page_simple(self):
        url = "https://the-internet.herokuapp.com/upload"
        self.open(url)

    def open_upload_page_hidden(self):
        url = "https://practice.automationbro.com/cart/"
        self.open(url)
