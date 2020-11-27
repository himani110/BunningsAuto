import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.MainPage import MainPage
from Pages.SignInPage import SignInPage
import time
import utilities as U
import Constant as C

driver = webdriver.Chrome()  # type: WebDriver


def test_main_page():
    mp = MainPage(driver)
    mp.test_title()
    driver.save_screenshot(C.ScreenShot_Title)
    # To check the result on search of value : drill , 1234 , blank value
    for i in [1, 2, 3]:
        var = ["drill", "1234", "  ", 1]
        print (var[i - 1])
        mp.search_type(var[i - 1])
        time.sleep(2)
        mp.GoTo_Main_Page()
        message = "TC_1: Executed with search value as  successfully"
        U.log("INFO", C.message, C.log_file)
    # mp.clear_recent()


def down():
    driver.quit()


set_up()
test_main_page()
down()
