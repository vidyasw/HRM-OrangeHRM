from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class JobCategories():

    def __init__(self, driver):
        self.driver = driver
        self.admin_xpath = "//*[@id = 'menu_admin_viewAdminModule']"
        self.job_xpath = "//*[@id='menu_admin_Job']"
        self.job_category_xpath = "//*[@id='menu_admin_jobCategory']"
        self.add_btn_name = "btnAdd"
        self.job_category_table_xpath = "//*[@id='resultTable']"
        self.job_category_input_name = "jobCategory[name]"
        self.save_btn_id = "btnSave"

    def Login_Job_Categories(self):
        admin = self.driver.find_element_by_xpath(self.admin_xpath)
        job = self.driver.find_element_by_xpath(self.job_xpath)
        job_category = self.driver.find_element_by_xpath(self.job_category_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(job).move_to_element(job_category).click().perform()
        return self.driver.find_element_by_tag_name("h1").text

    def open_Add_Job_Category_form(self):
        self.driver.find_element_by_name(self.add_btn_name).click()
        return self.driver.find_element_by_tag_name("h1").text

    def enter_job_category_name(self,job_category_name):
        self.driver.find_element_by_name(self.job_category_input_name).clear()
        self.driver.find_element_by_name(self.job_category_input_name).send_keys(job_category_name)

    def save_job_category(self):
        self.driver.find_element_by_id(self.save_btn_id).click()

    def get_rowCount(self,table_xpath):
        table = self.driver.find_element_by_xpath(table_xpath)
        return len(table.find_elements(By.TAG_NAME,"tr")) - 1

    def verify_job_category(self,job_category_name):
        table = self.driver.find_element_by_xpath(self.job_category_table_xpath)
        for r in range (1,self.get_rowCount(self.job_category_table_xpath)):
            if job_category_name == table.find_element_by_xpath("//tr[" + str(r) + "]/td[2]").text:
                return True
        return False

    def open_edit_job_category_form(self,job_category_toedit):
        table = self.driver.find_element_by_xpath(self.job_category_table_xpath)
        table.find_element_by_link_text(job_category_toedit).click()
        if "Edit Job Category" in self.driver.find_element_by_tag_name("h1").text:
            print("Edit Job Category is opened successfully")