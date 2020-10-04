from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PayGrades():

    def __init__(self,driver):
        self.driver = driver
        self.admin_xpath = "//*[@id = 'menu_admin_viewAdminModule']"
        self.job_xpath = "//*[@id='menu_admin_Job']"
        self.pay_grade_menu_xpath = "//*[@id='menu_admin_viewPayGrades']"
        self.add_btn_name = "btnAdd"
        self.pay_grade_input_id = "payGrade_name"
        self.btn_save_id = "btnSave"
        self.edit_pay_garde_id = "payGrade"
        self.edit_pay_grade_heading_id = "payGradeHeading"
        self.Add_currency_heading_id = "currencyHeading"
        self.assigned_currencies_heading_id = "currencyListHeading"
        self.add_currency_btn_id = "btnAddCurrency"
        self.add_edit_currency_form_xpath = "//*[@id='addEditCurrency']"
        self.currency_input_xpath = "//*[@id='payGradeCurrency_currencyName']"
        self.minsal_input_id = "payGradeCurrency_minSalary"
        self.maxsal_input_id = "payGradeCurrency_maxSalary"
        self.save_currency_btn_id = "btnSaveCurrency"
        self.currency_form_xpath = "//*[@id='currency']"
        self.currency_table_xpath = "//*[@id='tblCurrencies']"
        self.btn_cancel_id = "btnCancel"
        self.pay_grade_table_xpath = "//*[@id='resultTable']"

    def Login_pay_grade(self):
        admin = self.driver.find_element_by_xpath(self.admin_xpath)
        job = self.driver.find_element_by_xpath(self.job_xpath)
        pay_grade = self.driver.find_element_by_xpath(self.pay_grade_menu_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(job).move_to_element(pay_grade).click().perform()
        return self.driver.find_element_by_tag_name("h1").text

    def Login_Add_pay_grade_form(self):
        self.driver.find_element_by_name(self.add_btn_name).click()
        return self.driver.find_element_by_tag_name("h1").text

    def enter_pay_grade(self,pay_grade_level):
        self.driver.find_element_by_id(self.pay_grade_input_id).clear()
        self.driver.find_element_by_id(self.pay_grade_input_id).send_keys(pay_grade_level)

    def save_pay_grade(self):
        self.driver.find_element_by_id(self.btn_save_id).click()

    def open_Add_currency_form(self):
        self.driver.find_element_by_id(self.add_currency_btn_id).click()
        return self.driver.find_element_by_id(self.Add_currency_heading_id).text

    def enter_currency(self,currency):
        parentbox = self.driver.find_element_by_xpath(self.add_edit_currency_form_xpath)
        parentbox.find_element_by_xpath(self.currency_input_xpath).send_keys(currency)

    def enter_salary(self,min_salary,max_salary):
        parentbox = self.driver.find_element_by_xpath(self.add_edit_currency_form_xpath)
        parentbox.find_element_by_id(self.minsal_input_id).send_keys(min_salary)
        parentbox.find_element_by_id(self.maxsal_input_id).send_keys(max_salary)

    def save_currency_salary_details(self):
        parentbox = self.driver.find_element_by_xpath(self.add_edit_currency_form_xpath)
        '''click save button to save currency'''
        parentbox.find_element_by_id(self.save_currency_btn_id).click()

    def get_rowCount(self,table_xpath):
        table = self.driver.find_element_by_xpath(table_xpath)#self.currency_table_xpath)
        return len(table.find_elements(By.TAG_NAME,"tr")) - 1

    def get_colCount(self,table_xpath):
        table = self.driver.find_element_by_xpath(table_xpath) #self.currency_table_xpath)
        return len(table.find_elements_by_xpath("//tr[1]/td"))

    def get_Assigned_currency_title(self):
        return self.driver.find_element_by_id(self.assigned_currencies_heading_id).text

    def get_assigned_currency_details(self):
        parentBox1 = self.driver.find_element_by_xpath(self.currency_form_xpath)
        list_assigned_currencies = []
        table = parentBox1.find_element_by_xpath(self.currency_table_xpath)
        for r in range(1, len(table.find_elements(By.TAG_NAME, "tr"))):
            string = "Row No- " + str(r)
            for c in range(1,len(table.find_elements_by_xpath("//tr[1]/td"))+1):
                value = table.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text
                if len(value) != 0:
                    # print(value)
                    string = string + (": " + value)
            list_assigned_currencies.append(string)
        print(list_assigned_currencies)
        return list_assigned_currencies

    def verify_assigned_currency(self,currency_unit,min_salary,max_salary):
        currency = currency_unit.split('-')
        salary_min = str(min_salary) + ".00"
        salary_max = str(max_salary) + ".00"
        currency_compare = currency[len(currency) - 1].strip()
        salary_min_compare = salary_min.strip()
        salary_max_compare = salary_max.strip()
        list_assigned_currencies = self.get_assigned_currency_details()
        # print(list_assigned_currencies)
        for item in list_assigned_currencies:
            list1 = item.split(':')
            row_no = None
            for list_item in list1:
                bad_chars = [',']
                for i in bad_chars:
                    list_item = list_item.replace(i, '')
                if "Row No-" in list_item:
                    row_no = list_item
                if list_item.strip() == currency_compare or list_item.strip() == salary_min_compare or \
                   list_item.strip() == salary_max_compare:
                    print(list_item + " has added successfully and available at " + row_no)

    def close_pay_grade_form(self):
        self.driver.find_element_by_id(self.btn_cancel_id).click()
        return self.driver.find_element_by_tag_name("h1").text

    def verify_pay_grade(self,pay_grade):
        table = self.driver.find_element_by_xpath(self.pay_grade_table_xpath)
        for r in range(1, self.get_rowCount(self.pay_grade_table_xpath)):
            # for c in range(1, self.get_colCount() + 1):
            if pay_grade == table.find_element_by_xpath("//tr[" + str(r) + "]/td[2]").text:
                # print(table.find_element_by_xpath("//tr[" + str(r) + "]/td[2]").text)
                return True
        return False

    def open_edit_pay_grade_form(self,pay_garde_edit):
        table = self.driver.find_element_by_xpath(self.pay_grade_table_xpath)
        table.find_element_by_link_text(pay_garde_edit).click()
        if "Edit Pay Grade" in self.driver.find_element_by_tag_name("h1").text:
            print("Edit Pay Grade is opened successfully")

    def click_edit_btn(self):
        self.driver.find_element_by_id(self.btn_save_id).click()