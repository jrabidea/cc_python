__author__ = 'jrabidea'
import unittest
import time
import datetime
from selenium import webdriver
from cookie_panel import *
from middle_panel_menu import *



class CookieClicker(unittest.TestCase):

    minutes = 0

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://orteil.dashnet.org/cookieclicker/"

    def timer(self):
        start_time = time.time()
        elapsed_time = time.time() - start_time
        if elapsed_time > 59:
            self.minutes += self.minutes
            start_time = time.time()


    def test_play_cookie_clicker(self):
        last_save = 0
        driver = self.driver
        driver.get(self.base_url)
        cookie_pane = CookiePanel(driver)
        mid_pane = Menu(driver)
        mid_pane.turn_off_graphics()
        while True:
            self.timer()
            cookie_pane.click_cookie()



    def tearDown(self):
        self.driver.quit()

