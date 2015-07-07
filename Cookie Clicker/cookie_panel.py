__author__ = 'jrabidea'

from selenium.webdriver.common.by import By

from base_page_object import *


class CookiePanel(BasePageObject):
    def __init__(self, driver):
        super(CookiePanel, self).__init__(driver)

    def click_cookie(self):
        cookie = By.ID, "bigCookie"
        self.find_element(cookie).click()

    def change_bakery_name(self):
        bake_field = By.ID, "bakeryName"
        self.find_element(bake_field).click()
        self.find_element(bake_field).send_keys()

    def name_backery(self):
        random_button = By.ID, "promptOption1"
        self.wait(random_button, 30)
        self.find_element(random_button).click()
