__author__ = 'jrabidea'

from base_page_object import *
from selenium.webdriver.common.by import By

class Menu(BasePageObject):

    menu_modal = By.ID, "menu"
    menu = By.ID, "prefsButton"
    menu_close = By.XPATH, "//div[@onclick = 'Game.ShowMenu();']"
    load_save_modal = By.ID, "prompt"
    text_area = By.ID, "textareaPrompt"

    def __init__(self, driver):
        super(Menu, self).__init__(driver)

    def save_game(self):
        export_save = By.XPATH,"//a[@onclick = 'Game.ExportSave();']"
        all_done = By.ID, "promptOption0"
        self.find_element(self.menu).click()
        self.wait(self.menu_modal, 20)
        self.find_element(export_save).click()
        self.wait(self.text_area, 20)
        with open("Cookie_Clicker.txt", "w+") as save:
            save.write(self.find_element(self.text_area).text)
        self.find_element(all_done).click()
        self.find_element(self.menu_close).click()

    def import_save(self):
        import_save = By.XPATH, "//a[@onclick = 'Game.ImportSave();']"
        load_button = By.ID, "promptOption0"
        self.find_element(self.menu).click()
        self.wait(self.menu_close, 20)
        self.find_element(import_save).click()
        self.wait(self.text_area, 20)
        with open("Cookie_Clicker.txt", "r") as load:
            code = load.read()
        self.find_element(self.text_area).send_keys(code)
        self.find_element(load_button).click()
        self.find_element(self.menu_close).click()

    def turn_off_graphics(self):
        fancy_graphics = By.ID, "fancyButton"
        particles_button = By.ID, "particlesButton"
        milk_button = By.ID, "milkButton"
        cursors_button = By.ID, "cursorsButton"
        settings = [fancy_graphics, particles_button, milk_button, cursors_button]
        self.find_element(self.menu).click()
        self.wait(cursors_button, 20)
        for d in settings:
            self.find_element(d).click()
        self.find_element(self.menu_close).click()





