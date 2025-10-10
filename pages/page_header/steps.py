import allure

from .locators import HeaderLocators
from ..base_page import BasePage

class PageHeader(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = HeaderLocators

    def click_on_button_private_cabinet(self):
        with allure.step('Кликнуть по кнопке "Личный кабинет"'):
            self.wait_and_click(self.driver, locator=self.locators.button_private_cabinet)

    def click_on_button_logo(self):
        with allure.step('Кликнуть по кнопке "Личный кабинет"'):
            self.wait_and_click(self.driver, locator=self.locators.button_logo)

    def click_on_button_constructor(self):
        with allure.step('Кликнуть по кнопке "Личный кабинет"'):
            self.wait_and_click(self.driver, locator=self.locators.button_open_constructor)
