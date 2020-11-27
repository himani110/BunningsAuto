import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import utilities as U

emailid = "hdummy030@gmail.com"
password = "pass@123"
term = "My Profile at Bunnings"
Email_locator = "body_1_LoginForm_UserName"
Password_locator = "body_1_LoginForm_Password"
signin_button_locator = "LoginButton"
message = "Exception Occurred"
log_file = "../Logs/log.txt"


class SignInPage:

    def __init__(self, drv):
        self.drv = drv
        # self.wait_variable = W(self.drv, self.wait_time_out)

    def Login(self):

        try:
            self.Click_SignIn()
            self.drv.find_element(By.ID, "body_1_LoginForm_UserName").click()
            self.drv.find_element(By.ID, "body_1_LoginForm_UserName").sendkeys(emailid)

            self.drv.find_element(By.ID, "body_1_LoginForm_Password").click()
            self.drv.find_element(By.ID, "body_1_LoginForm_Password").sendkeys(password)

            self.drv.find_element(By.ID, "LoginButton").click()
            time.sleep(2)
            self.wait_variable.until(E.title_contains(self.term))
        except NoSuchElementException:
            U.log("INFO: ", message, log_file)
            pass

    def Click_SignIn(self):
        self.drv.find_element(By.XPATH, "//div[2]/ul/li/a/span").click()
