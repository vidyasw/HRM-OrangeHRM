from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from OrangeHRM_Common.OrangeHRM_InputManagement.Text_utility import Text_utilities
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj
from Utils import Utils as utils


class JobTitles():

    src_file = utils.src_file
    dest_file = utils.dest_file

    def __init__(self,driver):
        self.driver = driver
        self.admin_xpath = "//*[@id = 'menu_admin_viewAdminModule']"
        self.job_xpath = "//*[@id='menu_admin_Job']"
        self.job_title_xpath = "//*[@id='menu_admin_viewJobTitleList']"
        self.add_btn_id = "btnAdd"
        self.add_job_title_form_title_id = "saveHobTitleHeading"
        self.job_title_text_name = "jobTitle[jobTitle]"
        self.job_desc_text_id = "jobTitle_jobDescription"
        self.job_spec_id = "jobTitle_jobSpec"
        self.job_note_id = "jobTitle_note"
        self.job_save_btn_name = "btnSave"
        self.job_table_xpath = "//*[@id='resultTable']"
        self.edit_btn_name = "btnSave"

    def Login_jobTitles_Tab(self):
        admin = self.driver.find_element_by_xpath(self.admin_xpath)
        job = self.driver.find_element_by_xpath(self.job_xpath)
        job_title = self.driver.find_element_by_xpath(self.job_title_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(job).move_to_element(job_title).click().perform()
        return self.driver.find_element_by_tag_name("h1").text

    def navigate_jobTitles_form(self):
        self.driver.find_element_by_id(self.add_btn_id).click()
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_id(self.add_job_title_form_title_id).text

    def enter_jobTitle(self,job_title):
        self.driver.find_element_by_name(self.job_title_text_name).clear()
        self.driver.find_element_by_name(self.job_title_text_name).send_keys(job_title)

    def enter_jobDescription(self,job_desc):
        self.driver.find_element_by_id(self.job_desc_text_id).clear()
        self.driver.find_element_by_id(self.job_desc_text_id).send_keys(job_desc)

    def upload_jobSpecification(self,spec_role):
        Text_utilities.create_specifications(JobTitles.src_file,JobTitles.dest_file,spec_role)
        self.driver.find_element_by_id(self.job_spec_id).send_keys(JobTitles.dest_file)

    def enter_job_title_note(self,notes):
        self.driver.find_element_by_id(self.job_note_id).clear()
        self.driver.find_element_by_id(self.job_note_id).send_keys(notes)

    def saveTitle(self):
        self.driver.find_element_by_name(self.job_save_btn_name).click()
        self.driver.implicitly_wait(1)

    def get_rowCount(self):
        table = self.driver.find_element_by_xpath(self.job_table_xpath)
        # print("Row count :",len(table.find_elements_by_tag_name("tr")) - 1)
        return len(table.find_elements(By.TAG_NAME,"tr")) - 1

    def get_colCount(self):
        table = self.driver.find_element_by_xpath(self.job_table_xpath)
        # print("col count:",len(table.find_elements_by_xpath("//tr[2]/td")))
        return len(table.find_elements_by_xpath("//tr[2]/td"))

    def get_job_titles(self):
        list_titles = []
        table = self.driver.find_element_by_xpath(self.job_table_xpath)
        for r in range(2, self.get_rowCount()):
            for c in range(1, self.get_colCount()):
                value = table.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text
                if len(value) !=0:
                    list_titles.append(value)
        logger_obj.info("List of Titles from get_job_titles" + str(list_titles))
        return list_titles

    def navigate_edit_job_title_form(self,job_title):
        list_job_titles = self.get_job_titles()
        if job_title in list_job_titles:
            self.driver.find_element_by_link_text(job_title).click()
            self.driver.implicitly_wait(1)
            return self.driver.find_element_by_tag_name("h1").text
        else:
            logger_obj.debug(job_title + " is not present")

    def edit_job_titles(self,job_title,job_description,job_notes):
        self.driver.find_element_by_name(self.edit_btn_name).click()
        if "Edit Job Title" in self.driver.find_element_by_tag_name("h1").text:
            print("navigation to Edit Job Title is successful")
        else:
            logger_obj.debug(job_title + " is not available")

        self.enter_jobDescription(job_description+ " -updated")
        self.enter_job_title_note(job_notes+ " -updated")
        self.saveTitle()
        return self.verify_job_description(job_title,job_description+" -updated")

    def verify_job_description(self,job_title,job_desc):
        validated_title = False
        validated_desc = False
        table = self.driver.find_element_by_xpath(self.job_table_xpath)
        for r in range(2, self.get_rowCount()):
            for c in range(1, self.get_colCount() + 1):
                value = table.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text
                if len(value) != 0 and value == job_title:
                    #print(value)
                    validated_title = True
                    #print(validated_title)
                if value == job_desc:
                    #print(value)
                    validated_desc = True
                    #print(validated_desc)
                    break
        return validated_title and validated_desc
