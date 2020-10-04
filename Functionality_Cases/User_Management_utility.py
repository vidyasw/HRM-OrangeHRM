from PageObjects.OrangeHRM_AdminPages.UserManagement.UsersManagement_Page import UserManagements


class User_management_utility():

    def __init__(self,driver):
        self.driver = driver

    def navigate_Users(self):
        user_mgmt = UserManagements(self.driver)
        user_nav_title = user_mgmt.Login_users_Tab()
        if user_nav_title == "System Users":
            print("Navigation to user Management is successful")
        else:
            print("Failed to navigate user Management")
        return user_nav_title

    def Collapse_System_users_Tab(self):
        user_mgmt = UserManagements(self.driver)
        user_mgmt.collapse_systemUsers()

    def get_list_Users(self):
        user_mgmt = UserManagements(self.driver)
        return user_mgmt.get_user_list()

    def delete_user(self,username,confirmation):
        user_mgmt = UserManagements(self.driver)
        user_mgmt.delete_user(username,confirmation)

    def select_user(self,username):
        user_mgmt = UserManagements(self.driver)
        user_mgmt.select_user(username)