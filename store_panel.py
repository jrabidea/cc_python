__author__ = 'jrabidea'

from selenium.webdriver.common.by import By

from base_page_object import *

class StoreUpgrades(BasePageObject):

    enabled = "product unlocked enabled"
    crate_enabled = "crate upgrade enabled"

    def buy_products(self):

        if self.get_class(0) == self.enabled and self.get_prod_owned(0) < 21:
            self.click_upgrade(0)
        elif self.get_class(1) == self.enabled and self.get_prod_owned(1) < 21:
            self.click_upgrade(1)
        elif self.get_class(2) == self.enabled and self.get_prod_owned(2) < 21:
            self.click_upgrade(2)
        elif self.get_class(3) == self.enabled and self.get_prod_owned(3) < 21:
            self.click_upgrade(3)

    def get_class(self, index):

        self.index = index

        return self.get_product_element(index).get_attribute("className")

    def get_prod_owned(self, index):

        self.index = index

        prod_owned = ["productOwned0", "productOwned1", "productOwned2", "productOwned3"]

        if self.driver.find_element_by_id(prod_owned[index]).text == "":
            return 0
        else:
            return int(self.driver.find_element_by_id(prod_owned[index]).text)

    def click_upgrade(self, index):

        self.get_product_element(index).click()

    def get_product_element(self, index):

        self.index = index

        products = ["product0","product1","product2","product3"]

        return self.driver.find_element_by_id(products[index])

    def buy_store_upgrade(self):

        store_upgrade = By.ID, "upgrade0"

        if self.find_element(store_upgrade).get_attribute("className") == self.crate_enabled:
            self.find_element(store_upgrade).click()