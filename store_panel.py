__author__ = 'jrabidea'

from selenium.webdriver.common.by import By

from base_page_object import *

class StoreUpgrades(BasePageObject):

    enabled = "product unlocked enabled"
    crate_enabled = "crate upgrade enabled"
    limit = 10
    limit_two = 10
    total_products = 0

    def buy_products(self):

        if self.get_class(0) == self.enabled and self.get_prod_owned(0) < self.limit:
            self.click_upgrade(0)
        elif self.get_class(1) == self.enabled and self.get_prod_owned(1) < self.limit:
            self.click_upgrade(1)
        elif self.get_class(2) == self.enabled and self.get_prod_owned(2) < self.limit:
            self.click_upgrade(2)
        elif self.get_class(3) == self.enabled and self.get_prod_owned(3) < self.limit:
            self.click_upgrade(3)
        elif self.get_class(4) == self.enabled and self.get_prod_owned(4) < self.limit:
            self.click_upgrade(4)
        elif self.get_class(5) == self.enabled and self.get_prod_owned(5) < self.limit:
            self.click_upgrade(5)
        elif self.get_class(6) == self.enabled and self.get_prod_owned(6) < self.limit:
            self.click_upgrade(6)
        elif self.get_class(7) == self.enabled and self.get_prod_owned(7) < self.limit:
            self.click_upgrade(7)
        elif self.get_class(8) == self.enabled and self.get_prod_owned(8) < self.limit:
            self.click_upgrade(8)
        elif self.get_class(9) == self.enabled and self.get_prod_owned(9) < self.limit:
            self.click_upgrade(9)

    def get_class(self, index):

        self.index = index

        return self.get_product_element(index).get_attribute("className")

    def get_prod_owned(self, index):

        self.index = index

        prod_owned = ["productOwned0", "productOwned1", "productOwned2",
                      "productOwned3", "productOwned4", "productOwned5",
                      "productOwned6", "productOwned5", "productOwned6",
                      "productOwned7", "productOwned8", "productOwned9"]

        for a in prod_owned:
            if self.driver.find_element_by_id(a).text == "":
                self.total_products += 0
            else:
                bought_num = int(self.driver.find_element_by_id(a).text)
                self.total_products += bought_num

        if self.driver.find_element_by_id(prod_owned[index]).text == "":
            return 0
        else:
            return int(self.driver.find_element_by_id(prod_owned[index]).text)

    def click_upgrade(self, index):

        self.get_product_element(index).click()

    def get_product_element(self, index):

        self.index = index

        products = ["product0","product1","product2","product3", "product4",
                    "product5", "product6", "product7", "product8",
                    "product9"]

        return self.driver.find_element_by_id(products[index])

    def buy_store_upgrade(self):

        store_upgrade = By.ID, "upgrade0"

        if self.find_element(store_upgrade).get_attribute("className") == self.crate_enabled:
            self.find_element(store_upgrade).click()


    def set_limit(self, total_products):

        self.total_products = total_products

        if total_products == 80:
            limit = 20
        elif total_products == 210:
            limit = 50
        elif total_products == 490:
            limit = 100