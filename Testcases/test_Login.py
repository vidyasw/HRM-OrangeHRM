import os
import time
import pytest
from selenium import webdriver
from PageObjects.OrangeHRM_LoginPages.Login_Page import LoginPages
from PageObjects.OrangeHRM_HomePags.HomePage import HomePages
from PageObjects.OrangeHRM_LoginPages.Forgot_Password_Page import ForgotPasswords
from Utils import Utils as utils
from OrangeHRM_Common.OrangeHRM_ExceptionHandling import ExceptionUtility
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj


@ pytest.mark.usefixtures("test_setup")
class TestLogin:

    @pytest.fixture(scope="class")
    def test_setup(self):
        logger_obj.info("setup called")
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Vidyashri\\PythonSeleniumProjects\\Drivers\\chromedriver_win32"
                                                  "\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        logger_obj.info("teardown called")
        driver.close()
        driver.quit()
        logger_obj.info("Test Completed")

    def test_1validation_login(self,test_setup):
        try:
            logger_obj.info("1validation_login called")
            # driver = self.driver
            driver.get(utils.url)
            driver.set_page_load_timeout(10)
            login = LoginPages(driver)
            login.enter_username("")
            login.click_login()
            time.sleep(1)
            empty_username = login.warning_emptyUsername()
            if empty_username == utils.msg_username_empty:
                print("Username is empty")
            else:
                print("Username is not empty")
            assert empty_username == utils.msg_username_empty

            login.enter_username(utils.valid_username)
            login.enter_password("")
            login.click_login()
            time.sleep(1)
            empty_password = login.warning_emptyPassword()
            if empty_password == utils.msg_password_empty:
                print("Password is empty")
            else:
                print("Password is not empty")
            assert empty_password == utils.msg_password_empty

            driver.refresh()
            login.enter_username(utils.invalid_username)
            login.enter_password(utils.invalid_password)
            login.click_login()
            wrong_cred = login.warning_wrongCredentials()
            if wrong_cred == utils.msg_Invalid_credentials:
                print("Invalid credentials")
            else:
                print("Valid credentials")
            assert wrong_cred == utils.msg_Invalid_credentials
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_2forgotPassword_click(self,test_setup):
        try:
            logger_obj.info("2forgotPassword_click called")
            # driver = self.driver
            forgot_password = ForgotPasswords(driver)
            heading = forgot_password.forgot_password_link_click()
            if heading in utils.heading_ForgotYourPassword:
                print("Forgot Password is navigated successfully")
            else:
                print("Failed to navigate to Forgot Password")
            assert heading == utils.heading_ForgotYourPassword
            forgot_password.enter_username("")
            forgot_password.return_loginPage()
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_3login(self,test_setup):
        try:
            logger_obj.info("3login called")
            # driver = self.driver
            driver.get(utils.url)
            login = LoginPages(driver)
            login.enter_username(utils.valid_username)
            login.enter_password(utils.valid_password)
            login.click_login()
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_4logout(self,test_setup):
        try:
            logger_obj.info("4logout called")
            # driver = self.driver
            homepage = HomePages(driver)
            homepage.click_welcome()
            homepage.click_logout()
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)