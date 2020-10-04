class LoginPages():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = "txtUsername"
        self.password_text_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.warning_msg_no_credentered_xpath = "//*[@id='spanMessage']"
        self.forgotPassword_link_id = "forgotPasswordLink"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def warning_emptyUsername(self):
        msg = self.driver.find_element_by_xpath(self.warning_msg_no_credentered_xpath).text
        return msg

    def warning_emptyPassword(self):
        msg = self.driver.find_element_by_xpath(self.warning_msg_no_credentered_xpath).text
        return msg

    def warning_wrongCredentials(self):
        msg = self.driver.find_element_by_xpath(self.warning_msg_no_credentered_xpath).text
        return msg

    def click_forgotPassword(self):
        self.driver.find_element_by_id(self.forgotPassword_link_id).click()