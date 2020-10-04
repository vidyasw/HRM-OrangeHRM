import os
from Functionality_Cases.Job_utility import Job_utility
# from PageObjects.OrangeHRM_LoginPages.Login_Page import LoginPages
# from PageObjects.OrangeHRM_HomePags.HomePage import HomePages
# from selenium import webdriver
from Utils import Utils as utils
import pytest
from OrangeHRM_Common.OrangeHRM_ExceptionHandling import ExceptionUtility
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj


@ pytest.mark.usefixtures("test_setup")
class TestJob:

    # path = "E:\\HRM-OrangeHRM\\OrangeHRM_Common\\OrangeHRM_input_Sheet.xlsx"
    # sheet_Inputs = "Inputs"
    # sheet_Job_Titles = "Job_Titles"
    # sheet_Pay_Grade = "Pay_Grade"
    # sheet_Emp_status = "Emp_status"
    # sheet_Job_Category = "Job_Category"
    # sheet_Work_Shift = "Work_Shift"
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

    def test_Add_Job_Title(self):
        try:
            logger_obj.info("test_1Add_Job_Title called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.navigate_jobTitles()
            list_titles_before_add = job_mgmt.get_job_title_list()
            job_mgmt.add_job_title(utils.job_title_cto,utils.job_spec_cto,utils.job_description_cto,utils.job_notes_cto)
            list_titles_after_add = job_mgmt.get_job_title_list()
            if int(len(list_titles_after_add)) > int(len(list_titles_before_add)) and utils.job_title_cto in list_titles_after_add:
                print(utils.job_title_cto + " added Successfully")
            else:
                print("Failed to add " + utils.job_title_cto)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Edit_Job_Title(self):
        try:
            logger_obj.info("test_2Edit_Job_Title called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.navigate_jobTitles()
            edited = job_mgmt.edit_job_title(utils.job_title_cto,utils.job_description_cto,utils.job_notes_cto)
            if edited is True:
                print(utils.job_title_cto + " edited successfully")
            else:
                print("Failed to edit " + utils.job_title_cto)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Add_PayGrade(self):
        try:
            logger_obj.info("test_3Add_PayGrade called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_payGrades()
            job_mgmt.add_payGrades(utils.pay_grade_level,utils.pay_currency,utils.min_salary,utils.max_salary)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Edit_PayGrade(self):
        try:
            logger_obj.info("test_4Edit_PayGrade called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_payGrades()
            job_mgmt.edit_payGrades(utils.pay_grade_level,utils.edit_pay_grade_name)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Add_Employment_status(self):
        try:
            logger_obj.info("test_5Add_Employment_status called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_employmentStatus()
            job_mgmt.add_empStatus(utils.emp_status_name)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Edit_Employment_status(self):
        try:
            logger_obj.info("6Edit_Employment_status called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_employmentStatus()
            job_mgmt.edit_empStatus(utils.emp_status_name,utils.emp_status_name_to_edit)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Add_Job_Categories(self):
        try:
            logger_obj.info("7Add_Job_Categories called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_jobCategories()
            job_mgmt.add_jobCategories(utils.job_category_it_professional)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Edit_Job_Categories(self):
        try:
            logger_obj.info("8Edit_Job_Categories called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_jobCategories()
            job_mgmt.edit_jobCategories(utils.job_category_it_professional,utils.job_category_it_professional_edit)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Add_Work_Shifts(self):
        try:
            logger_obj.info("test_9Add_Work_Shifts called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_workShifts()
            print(utils.shift_hrs_frm, utils.shift_hrs_to)
            job_mgmt.add_work_shift_details(utils.shift_name,"13:00","22:00")#utils.shift_hrs_frm,utils.shift_hrs_to)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)

    def test_Edit_Work_Shifts(self):
        try:
            logger_obj.info("test_10Edit_Work_Shifts called")
            driver = self.driver
            job_mgmt = Job_utility(driver)
            job_mgmt.login_workShifts()
            job_mgmt.edit_work_shift_details(utils.shift_name, utils.shift_name_to_edit)
        except Exception as e:
            logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
            logger_obj.exception("Error : ", exc_info=False)
            logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
            logger_obj.exception("Details --> " + str(e), exc_info=False)
            ExceptionUtility.call_exception_utility(exit_code=1)