from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Employment_status():

    def __init__(self, driver):
        self.driver = driver
        self.admin_xpath = "//*[@id = 'menu_admin_viewAdminModule']"
        self.job_xpath = "//*[@id='menu_admin_Job']"
        self.employee_status_xpath = "//*[@id='menu_admin_employmentStatus']"
        self.add_btn_name = "btnAdd"
        self.emp_status_input_name = "empStatus[name]"
        self.save_btn_id = "btnSave"
        self.emp_status_table_xpath = "//*[@id='resultTable']"
        self.btn_save_id = "btnSave"

    def Login_Employee_Status(self):
        admin = self.driver.find_element_by_xpath(self.admin_xpath)
        job = self.driver.find_element_by_xpath(self.job_xpath)
        employee_status = self.driver.find_element_by_xpath(self.employee_status_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(job).move_to_element(employee_status).click().perform()
        return self.driver.find_element_by_tag_name("h1").text

    def open_Add_Employment_Status_form(self):
        self.driver.find_element_by_name(self.add_btn_name).click()
        return self.driver.find_element_by_tag_name("h1").text

    def enter_emp_status(self,emp_status_name):
        self.driver.find_element_by_name(self.emp_status_input_name).clear()
        self.driver.find_element_by_name(self.emp_status_input_name).send_keys(emp_status_name)

    def save_emp_status(self):
        self.driver.find_element_by_id(self.save_btn_id).click()

    def get_rowCount(self,table_xpath):
        table = self.driver.find_element_by_xpath(table_xpath)#self.currency_table_xpath)
        return len(table.find_elements(By.TAG_NAME,"tr")) - 1

    def verify_emp_status(self,emp_status_name):
        table = self.driver.find_element_by_xpath(self.emp_status_table_xpath)
        for r in range (1,self.get_rowCount(self.emp_status_table_xpath)):
            if emp_status_name == table.find_element_by_xpath("//tr[" + str(r) + "]/td[2]").text:
                #print(value)
                #if value == emp_status_name:
                return True
        return False

    def open_edit_emp_status_form(self,emp_status_edit):
        table = self.driver.find_element_by_xpath(self.emp_status_table_xpath)
        table.find_element_by_link_text(emp_status_edit).click()
        if "Edit Employment Status" in self.driver.find_element_by_tag_name("h1").text:
            print("Edit Employment Status is opened successfully")