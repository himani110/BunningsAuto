import time
import utilities as U
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.MainPage import MainPage
from Pages.SignInPage import SignInPage
import Constant as C


driver = webdriver.Chrome()  # type: WebDriver


def clear_recent_search():
    mp = MainPage(driver)
    mp.test_title()
    U.log("INFO", C.message, C.log_file)
    driver.save_screenshot("image.png")
    mp.clear_recent()
    U.log("INFO", C.message, C.log_file)


def customer_log_recent_search():
    sp = SignInPage(driver)
    sp.Login()


def down():
    driver.quit()


clear_recent_search()
down()
