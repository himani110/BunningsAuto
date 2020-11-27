import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import Bunnings_TC_1 as B1
import Bunnings_TC_2 as B2
import Bunnings_TC_3 as B3

driver = webdriver.Chrome()  # type: WebDriver


def test_search_different_value():
    B1.test_main_page()
    driver.quit()


def test_clear_recent_search():
    B2.clear_recent_search()
    driver.quit()


def test_customer_log_recent_search():
    B3.customer_log_recent_search()
    driver.quit()
