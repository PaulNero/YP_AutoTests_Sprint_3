import allure

from .locators import PagePrivateCabinetLocators
from ..base_page import BasePage

class PagePrivateCabinet(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = PagePrivateCabinetLocators

    def click_on_button_exit(self):
        with allure.step('Нажать на кнопку "Выйти"'):
            self.wait_and_click(self.driver, locator=self.locators.button_exit_from_account)
