import pytest
from PageObjects.OrangeHRM_LoginPages.Login_Page import LoginPages
from PageObjects.OrangeHRM_HomePags.HomePage import HomePages
from Utils import Utils as utils


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="type in browser")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
            # executable_path="E:/Vidyashri/PythonSeleniumProjects/Drivers/chromedriver_win32/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Ie()
        # executable_path="E:/Vidyashri/PythonSeleniumProjects/Drivers/IEDriverServer_Win32_3.150.1/IEDriverServer.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(utils.url)
    login = LoginPages(driver)
    login.enter_username(utils.valid_username)
    login.enter_password(utils.valid_password)
    login.click_login()
    yield
    homepage = HomePages(driver)
    homepage.click_welcome()
    homepage.click_logout()
    driver.close()
    driver.quit()
    print("Test Completed call from conftest")