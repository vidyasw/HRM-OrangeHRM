# from OrangeHRM_Common.Excel_utility import Excel_utilities
# from selenium import webdriver
# from PageObjects.OrangeHRM_LoginPages.Login_Page import LoginPages
# from PageObjects.OrangeHRM_HomePags.HomePage import HomePages
from Functionality_Cases.User_Management_utility import User_management_utility
# from Utils import Utils as utils
import pytest
from OrangeHRM_Common.OrangeHRM_ExceptionHandling import ExceptionUtility
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj
import os


@ pytest.mark.usefixtures("test_setup")
class TestUserManagement:

    # path = "E:\\HRM-OrangeHRM\\OrangeHRM_Common\\OrangeHRM_input_Sheet.xlsx"
    # sheet_Inputs = "Inputs"
    # url = Excel_utilities.getvalue(path,sheet_Inputs,"application_url")

    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     print("setup called")
    #     global driver
    #     driver = webdriver.Chrome(executable_path="E:\\OrangeHRMProject\\Driver_Directory\\chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     login = LoginPages(driver)
    #     login.enter_username("Admin")
    #     login.enter_password("admin123")
    #     login.click_login()
    #     yield
    #     print("teardown called")
    #     homepage = HomePages(driver)
    #     homepage.click_welcome()
    #     homepage.click_logout()
    #     driver.close()

    def test_click_users(self):
        try:
            logger_obj.info("test_click_users called")
            driver = self.driver
            user_mgmt = User_management_utility(driver)
            user_mgmt.navigate_Users()
            user_mgmt.Collapse_System_users_Tab()

            users_list = user_mgmt.get_list_Users()
            print(users_list)
            print("User to Delete :",users_list[1])
            user_mgmt.select_user(users_list[1])
            #user_mgmt.delete_user(users_list[1],"Y")
            #self.assertFalse(user_mgmt.select_user(users_list[1]) == False, users_list[2] + " failed to delete")
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)
