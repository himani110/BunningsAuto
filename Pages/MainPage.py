from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import Constant as C
import utilities as U


class MainPage:
    wait_time_out = 5

    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = W(self.drv, self.wait_time_out)
        drv.get(C.base_url)
        drv.maximize_window()

    def test_title(self):
        checkTitle = self.drv.title
        print (checkTitle)
        assert C.title in self.drv.title

    def click_singin_link(self):
        self.drv.find_element(By.CSS_SELECTOR, ".header_navbar-link-copy:nth-child(3)").click()

    def search_type(self, search_item):

        if search_item == " " or search_item == "":
            self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").click()
            self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").send_keys(search_item)
            self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
            time.sleep(2)
            self.handle_simple_alert()
        else:
            self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").click()
            self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").send_keys(search_item)
            self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").send_keys(Keys.ENTER)

    def clear_recent(self):
        self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").click()
        self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").send_keys("up")
        self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        time.sleep(2)
        self.GoTo_Main_Page()
        self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/input").click()
        self.drv.find_element(By.XPATH, "//li[contains(.,'Clear recent searches')]").click()

    def handle_simple_alert(self):
        assert self.drv.switch_to.alert.text == "Please enter search keywords"
        element = self.drv.find_element(By.CSS_SELECTOR, ".hero-carousel_image-overlay_img")
        actions = ActionChains(self.drv)
        actions.move_to_element(element).perform()
        element = self.drv.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.drv)
        actions.move_to_element(element, 0, 0).perform()

    def GoTo_Main_Page(self):
        self.drv.find_element(By.CSS_SELECTOR, ".header_logo-image").click()
