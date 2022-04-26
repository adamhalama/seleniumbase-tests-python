from page_objects.upload_page import UploadPage


class UploadTest(UploadPage):

    def test_visible_upload(self):
        # open page
        UploadPage.open_upload_page_simple(self)

        # upload file
        self.choose_file(UploadPage.upload_file_tag_simple, UploadPage.logo_file_path)

        # click the upload button
        self.click(UploadPage.click_button_tag_simple)

        # assert file uploaded text
        self.assert_text(UploadPage.uploaded_text_simple, UploadPage.uploaded_tag_simple)


    def test_hidden_upload(self):

        # open page
        UploadPage.open_upload_page_hidden(self)


        # add js code for removing hidden class
        self.add_js_code(UploadPage.remove_hidden_class)

        # upload file
        self.choose_file(UploadPage.upload_file_tag_hidden, UploadPage.logo_file_path)

        # click the upload button
        self.click(UploadPage.click_button_tag_hidden)

        # assert file uploaded text
        # uploaded_text = self.get_text("#wfu_messageblock_header_1_label_1")
        # print(uploaded_text)
        # self.assert_true("uploaded successfully" in uploaded_text)

        # check uploaded text
        self.assert_text(UploadPage.uploaded_text_hidden, UploadPage.uploaded_tag_hidden)
