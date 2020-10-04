class ForgotPasswords():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = "securityAuthentication_userName"
        self.resetpwd_btn_id = "btnSearchValues"
        self.cancel_btn_id = "btnCancel"
        self.forgot_passwprd_link_text = "Forgot your password?"

    def forgot_password_link_click(self):
        self.driver.find_element_by_link_text(self.forgot_passwprd_link_text).click()
        return self.driver.find_element_by_tag_name("h1").text

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def return_loginPage(self):
        self.driver.find_element_by_id(self.cancel_btn_id).click()