from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserManagements():

    def __init__(self,driver):
        self.driver = driver
        self.admin_xpath = "//*[@id = 'menu_admin_viewAdminModule']"
        self.user_management_xpath = "//*[@id='menu_admin_UserManagement']"
        self.user_xpath = "//*[@id='menu_admin_viewSystemUsers']"
        self.toggle_tip_tip_css_selector = "a.toggle.tiptip"
        self.user_table_xpath = "//*[@id='resultTable']"
        self.delete_btn_id = "btnDelete"

    def Login_users_Tab(self):

        admin = self.driver.find_element_by_xpath(self.admin_xpath)
        user_management = self.driver.find_element_by_xpath(self.user_management_xpath)
        users = self.driver.find_element_by_xpath(self.user_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()
        return self.driver.find_element_by_tag_name("h1").text

    def collapse_systemUsers(self):
        self.driver.find_element_by_css_selector(self.toggle_tip_tip_css_selector).click()

    def get_rowCount(self):
        table = self.driver.find_element_by_xpath(self.user_table_xpath)
        # print("Row count :",len(table.find_elements_by_tag_name("tr")) - 1)
        return len(table.find_elements(By.TAG_NAME,"tr")) - 1

    def get_colCount(self):
        table = self.driver.find_element_by_xpath(self.user_table_xpath)
        # print("col count:",len(table.find_elements_by_xpath("//tr[2]/td")))
        return len(table.find_elements_by_xpath("//tr[2]/td"))

    def get_user_list(self):
        list_users =[]
        table = self.driver.find_element_by_xpath(self.user_table_xpath)
        print(self.get_rowCount())
        print(self.get_colCount())
        for r in range(2,self.get_rowCount()):
            for c in range(1,self.get_colCount()):
                value = table.find_element_by_xpath("//tr["+str(r)+"]/td["+str(c)+"]").text
                if "." not in value and value != "ESS" and len(value) != 0:
                    #print(value)
                    list_users.append(value)
        return list_users

    def select_user(self, username):
        table = self.driver.find_element_by_xpath(self.user_table_xpath)
        for r in range(2, self.get_rowCount()):
            for c in range(1, self.get_colCount()+1):
                if username in table.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text:
                    print("username",table.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text)
                    self.driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+str(r)+"]/td[1]").click()
                    break
        else:
            return False

    def delete_user(self,username,confirmation):
        self.select_user(username)
        self.driver.find_element_by_id(self.delete_btn_id).click()
        self.driver.implicitly_wait(1)
        #self.Handle_delete_Conf_Win(confirmation)

    def Handle_delete_Conf_Win(self, confirmation):
        # childwindow = self.driver.window_handles[1]
        # self.driver.switch_to.window(childwindow)
        # print(self.driver.find_element_by_tag_name("h3").text)

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.new_window_is_opened((By.CLASS_NAME, "deleteConfModal")))
        self.driver.switch_to.frame("deleteConfModal")

        win_title = self.driver.find_element_by_tag_name("h3").text
        print(win_title)       #OrangeHRM - Confirmation Required
        delete_conf_msg = self.driver.find_element_by_class_name("modal-body").text
        print(delete_conf_msg)
        if "Delete records?" in delete_conf_msg and confirmation == "Y":
            self.driver.find_element_by_id("dialogDeleteBtn").click()
        elif "Delete records?" in delete_conf_msg and confirmation == "N":
            self.driver.find_elemnent_by_class_name("btn reset").click()

    def add_user(self):
        pass
