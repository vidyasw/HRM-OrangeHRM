from PageObjects.OrangeHRM_AdminPages.Job.Job_JobTitle_Page import JobTitles
from PageObjects.OrangeHRM_AdminPages.Job.Job_PayGrade_Page import PayGrades
from PageObjects.OrangeHRM_AdminPages.Job.Job_JobCategory_Page import JobCategories
from PageObjects.OrangeHRM_AdminPages.Job.Job_EmploymentStatus_Page import Employment_status
from PageObjects.OrangeHRM_AdminPages.Job.Job_WorkShift_Page import WorkShifts
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj


class Job_utility():

    def __init__(self,driver):
        self.driver = driver

    def navigate_jobTitles(self):
        job_title_management = JobTitles(self.driver)
        job_nav_title = job_title_management.Login_jobTitles_Tab()
        if job_nav_title == "Job Titles":
            print("Navigation to Job Titles is successful")
        else:
            logger_obj.debug("Navigation failed to Job Titles")
        return job_nav_title

    def get_job_title_list(self):
        job_title_management = JobTitles(self.driver)
        return job_title_management.get_job_titles()

    def add_job_title(self,job_title,job_spec,job_desc,job_notes):
        job_title_management = JobTitles(self.driver)
        add_job_title_form_title = job_title_management.navigate_jobTitles_form()
        if add_job_title_form_title == "Add Job Title":
            print("Add Title navigation is successful")
        else:
            logger_obj.debug("Failed to navigate Add Title form")
        job_title_management.enter_jobTitle(job_title)
        job_title_management.enter_jobDescription(job_desc)
        job_title_management.upload_jobSpecification(job_spec)
        job_title_management.enter_job_title_note(job_notes)
        job_title_management.saveTitle()

    def edit_job_title(self,job_title,job_desc,job_notes):
        job_title_management = JobTitles(self.driver)
        edit_job_title_form_title = job_title_management.navigate_edit_job_title_form(job_title)
        if edit_job_title_form_title == "Edit Job Title":
            print(edit_job_title_form_title + "successfully navigated")
        else:
            logger_obj.debug("Failed to navigate Edit Job Title form")
        edited = job_title_management.edit_job_titles(job_title,job_desc,job_notes)
        return edited

    def login_payGrades(self):
        pay_grade_management = PayGrades(self.driver)
        job_nav_pay_grade = pay_grade_management.Login_pay_grade()
        if job_nav_pay_grade == "Pay Grades":
            print("Navigation to Pay Grade is successful")
        else:
            logger_obj.debug("Failed to navigate to Pay Grade")
        return job_nav_pay_grade

    def add_payGrades(self,pay_grade_name,currency_unit,salary_min,salary_max):
        pay_grade_management = PayGrades(self.driver)
        add_add_pay_grade_form_title = pay_grade_management.Login_Add_pay_grade_form()
        if add_add_pay_grade_form_title == "Add Pay Grade":
            print("Add Pay Grade form navigation is successful")
        else:
            logger_obj.debug("Failed to navigate Add Pay Grade")
        '''Save Pay_grade_level'''
        pay_grade_management.enter_pay_grade(pay_grade_name)
        pay_grade_management.save_pay_grade()
        if "Assigned Currencies" in pay_grade_management.get_Assigned_currency_title():
            print(pay_grade_name + " added successfully and Assigned currency table has displayed")
        else:
            logger_obj.debug("Failed to add Pay Grade")

        '''Add currency and salary limit'''
        add_currency_title = pay_grade_management.open_Add_currency_form()
        if "Add Currency" in add_currency_title:
            print(add_currency_title + " form opened successfully")
            pay_grade_management.enter_currency(currency_unit)
            pay_grade_management.enter_salary(salary_min, salary_max)
            pay_grade_management.save_currency_salary_details()
            pay_grade_management.verify_assigned_currency(currency_unit, salary_min, salary_max)

            add_pay_grade_form_title = pay_grade_management.close_pay_grade_form()
            if add_pay_grade_form_title == "Add Pay Grade":
                print("AddEditCurrency form closed successfully")
            else:
                logger_obj.debug("Failed to close AddEditCurrency form")
            added = pay_grade_management.verify_pay_grade(pay_grade_name)
            if added is True:
                print(pay_grade_name + " added successfully with currency,salary limit")
            else:
                logger_obj.debug(pay_grade_name + " failed to add with currency,salary limit")
        else:
            logger_obj.debug("Failed to open " + add_currency_title )

    def edit_payGrades(self,pay_garde_edit,new_pay_grade):
        pay_grade_management = PayGrades(self.driver)
        pay_grade_management.open_edit_pay_grade_form(pay_garde_edit)
        self.driver.implicitly_wait(1)
        pay_grade_management.click_edit_btn()
        pay_grade_management.enter_pay_grade(new_pay_grade)
        pay_grade_management.save_pay_grade()
        add_pay_grade_form_title = pay_grade_management.close_pay_grade_form()
        if add_pay_grade_form_title == "Pay Grades":
            print("Edit Pay Grades form closed successfully")
        edited = pay_grade_management.verify_pay_grade(new_pay_grade)
        if edited is True:
            print(new_pay_grade + " has edited successfully")
        else:
            logger_obj.debug("Failed to edit " + new_pay_grade)

    def login_employmentStatus(self):
        employment_status_management = Employment_status(self.driver)
        return employment_status_management.Login_Employee_Status()

    def add_empStatus(self,emp_status_name):
        employment_status_management = Employment_status(self.driver)
        add_emp_status = employment_status_management.open_Add_Employment_Status_form()
        if "Add Employment Status" in add_emp_status:
            print(add_emp_status + " navigated successfully")
        else:
            logger_obj.debug("Failed to debug " + add_emp_status)
        employment_status_management.enter_emp_status(emp_status_name)
        employment_status_management.save_emp_status()
        if employment_status_management.verify_emp_status(emp_status_name):
            print(emp_status_name + " added successfully")
        else:
            logger_obj.debug("Failed to "+ emp_status_name)

    def edit_empStatus(self,emp_status_Toedit,new_emp_status):
        employment_status_management = Employment_status(self.driver)
        employment_status_management.open_edit_emp_status_form(emp_status_Toedit)
        self.driver.implicitly_wait(1)
        employment_status_management.enter_emp_status(new_emp_status)
        employment_status_management.save_emp_status()
        edited = employment_status_management.verify_emp_status(new_emp_status)
        if edited is True:
            print(new_emp_status + " has edited successfully")
        else:
            logger_obj.debug("Failed to edit " + new_emp_status)

    def login_jobCategories(self):
        job_category_management = JobCategories(self.driver)
        return job_category_management.Login_Job_Categories()

    def add_jobCategories(self,job_category_name):
        job_category_management = JobCategories(self.driver)
        add_job_category = job_category_management.open_Add_Job_Category_form()
        if "Add Job Category" in add_job_category:
            print(add_job_category + " navigated successfully")
        else:
            logger_obj.debug("Failed to navigate " + add_job_category)
        job_category_management.enter_job_category_name(job_category_name)
        job_category_management.save_job_category()
        if job_category_management.verify_job_category(job_category_name):
            print(job_category_name + " added successfully")
        else:
            logger_obj.debug("Failed to edit " + job_category_name)

    def edit_jobCategories(self,job_category_edit,new_job_category):
        job_category_management = JobCategories(self.driver)
        job_category_management.open_edit_job_category_form(job_category_edit)
        self.driver.implicitly_wait(1)
        job_category_management.enter_job_category_name(new_job_category)
        job_category_management.save_job_category()
        edited = job_category_management.verify_job_category(new_job_category)
        if edited is True:
            print(new_job_category + " has edited successfully")
        else:
            logger_obj.debug("Failed to edit " + new_job_category)

    def login_workShifts(self):
        work_shifts_management = WorkShifts(self.driver)
        return work_shifts_management.Login_Work_Shifts()

    def add_work_shift_details(self,work_shift_name,work_hours_from,work_hours_to):
        work_shifts_management = WorkShifts(self.driver)
        add_work_shift = work_shifts_management.open_Add_work_shift_form()
        if "Add Work Shift" in add_work_shift:
            print(add_work_shift + " navigated successfully")
        else:
            logger_obj.debug("Failed to navigate " + add_work_shift)
        work_shifts_management.add_shift_name(work_shift_name)
        work_shifts_management.add_work_hours(work_hours_from, work_hours_to)
        work_shifts_management.assign_employees()
        work_shifts_management.save_work_shift_details()
        is_added = work_shifts_management.verify_work_shift_details(work_shift_name)
        # print(is_added)
        if is_added is True:
            print(work_shift_name + " added successfully")
        else:
            logger_obj.debug(work_shift_name + " failed to add")

    def edit_work_shift_details(self,work_shift_name,new_work_shift_name):
        work_shifts_management = WorkShifts(self.driver)
        work_shifts_management.open_edit_work_shift_form(work_shift_name)
        work_shifts_management.add_shift_name(new_work_shift_name)
        work_shifts_management.save_work_shift_details()
        is_edited = work_shifts_management.verify_work_shift_details(new_work_shift_name)
        if is_edited is True:
            print(new_work_shift_name + " edited successfully")
        else:
            logger_obj.debug(new_work_shift_name + " failed to edit")