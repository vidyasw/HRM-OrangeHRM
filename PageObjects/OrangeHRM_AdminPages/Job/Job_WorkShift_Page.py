from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class WorkShifts():

    def __init__(self, driver):
        self.driver = driver
        self.admin_xpath = "//*[@id = 'menu_admin_viewAdminModule']"
        self.job_xpath = "//*[@id='menu_admin_Job']"
        self.work_shifts_xpath = "//*[@id='menu_admin_workShift']"
        self.work_shifts_input_name = "workShift[name]"
        self.work_shift_table_xpath = "//*[@id='resultTable']"
        self.add_btn_name = "btnAdd"
        self.work_shift_from_id = "workShift_workHours_from"
        self.work_shift_to_id = "workShift_workHours_to"
        self.add_emp_table_xpath = "//*[@id='frmWorkShift']/fieldset/ol/table"
        self.add_link_text = "Add >>"
        self.save_btn_name = "btnSave"

    def Login_Work_Shifts(self):
        admin = self.driver.find_element_by_xpath(self.admin_xpath)
        job = self.driver.find_element_by_xpath(self.job_xpath)
        work_shifts = self.driver.find_element_by_xpath(self.work_shifts_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(job).move_to_element(work_shifts).click().perform()
        return self.driver.find_element_by_tag_name("h1").text

    def open_Add_work_shift_form(self):
        self.driver.find_element_by_name(self.add_btn_name).click()
        return self.driver.find_element_by_tag_name("h1").text

    def add_shift_name(self,shift_name):
        self.driver.find_element_by_name(self.work_shifts_input_name).clear()
        self.driver.find_element_by_name(self.work_shifts_input_name).send_keys(shift_name)

    def add_work_hours(self,work_hours_from,work_hours_to):
        self.driver.find_element_by_id(self.work_shift_from_id).send_keys(work_hours_from)
        self.driver.find_element_by_id(self.work_shift_to_id).send_keys(work_hours_to)

    def assign_employees(self):
        emp_add_table = self.driver.find_element_by_xpath(self.add_emp_table_xpath)
        # rows = len(emp_add_table.find_elements(By.TAG_NAME,"tr"))
        # cols = len(emp_add_table.find_elements_by_xpath("//tr[2]/td"))

        '''Get available emp List '''
        available_emp_row = self.driver.find_element_by_xpath("//*[@id='workShift_availableEmp']")
        list_ava_emps = available_emp_row.find_elements(By.TAG_NAME,"option")
        emp_list = []
        for list_item in list_ava_emps:
            emp_list.append(list_item.text)
        #print("List of available EMP List " + str(emp_list))

        '''Add employee '''
        list_ava_emps[0].click()
        emp_add_table.find_element_by_link_text(self.add_link_text).click()

        '''Get selected emp List'''
        selected_emp_row = self.driver.find_element_by_xpath("//*[@id='workShift_assignedEmp']")
        list_sel_emp = selected_emp_row.find_elements(By.TAG_NAME,"option")
        sel_emp_list = []
        for item in list_sel_emp:
            sel_emp_list.append(item.text)
        #print("List of selected EMP List " + str(sel_emp_list))

        if list_ava_emps[0].text in sel_emp_list:
            print(list_ava_emps[0].text + " is selected for the work shift")
        else:
            print("Failed to select " + list_ava_emps[2].text)

    def get_rowCount_from_work_shift_table(self,table_xpath):
        table = self.driver.find_element_by_xpath(table_xpath)
        return len(table.find_elements(By.TAG_NAME,"tr"))-1

    def verify_work_shift_details(self,work_shift_name):
        table = self.driver.find_element_by_xpath(self.work_shift_table_xpath)
        list_links = table.find_elements(By.TAG_NAME, "a")
        # print(list_links)
        for link in list_links:
            # print(link.text)
            if link.text == work_shift_name:
                return True
        return False

    def save_work_shift_details(self):
        self.driver.find_element_by_id(self.save_btn_name).click()

    def open_edit_work_shift_form(self,work_shift_toedit):
        table = self.driver.find_element_by_xpath(self.work_shift_table_xpath)
        table.find_element_by_link_text(work_shift_toedit).click()
        if "Edit Work Shift" in self.driver.find_element_by_tag_name("h1").text:
            print("Edit Work Shift is opened successfully")