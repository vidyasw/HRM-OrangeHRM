class HomePages():

    def __init__(self, driver):
        self.driver = driver
        self.welcome_partial_link_text = "Welcome " # Carlos"   # "Welcome Admin"
        self.logout_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_partial_link_text(self.welcome_partial_link_text).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_linkText).click()