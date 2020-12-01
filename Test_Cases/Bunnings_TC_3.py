import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.SignInPage import SignInPage
import Constant as C
import utilities as U


driver = webdriver.Chrome()  # type: WebDriver


def customer_log_recent_search():
    sp = SignInPage(driver)
    sp.Login()
    U.log("INFO", C.message, C.log_file)


def down():
    driver.quit()


customer_log_recent_search()
down()
