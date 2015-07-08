__author__ = 'jrabidea'
import unittest
import time
import datetime
from selenium import webdriver
from cookie_panel import *
from middle_panel_menu import *
from store_panel import *




class CookieClicker(unittest.TestCase):

    minutes = 0
    start_time = time.time()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://orteil.dashnet.org/cookieclicker/"

    def timer(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 60:
            self.minutes += 1
            self.start_time = time.time()

    def test_play_cookie_clicker(self):
        driver = self.driver
        driver.get(self.base_url)
        cookie_pane = CookiePanel(driver)
        mid_pane = Menu(driver)
        store = StoreUpgrades(driver)
        mid_pane.turn_off_graphics()
        mid_pane.import_save()
        while True:
            self.timer()
            cookie_pane.click_cookie()
            if self.minutes == 5:
                mid_pane.save_game()
                self.minutes = 0
            store.buy_products()
            store.buy_store_upgrade()
            mid_pane.close_notifications()
            mid_pane.click_golden_cookie()

    def tearDown(self):
        self.driver.quit()

