import allure

from .locators import ConstructorPageLocators
from ..base_page import BasePage

class PageConstructor(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = ConstructorPageLocators

    def click_on_button_enter_to_account_on_main_page(self):
        with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):
            self.wait_and_click(self.driver, locator=self.locators.button_enter_to_account_on_main_page)

    def click_on_button_private_cabinet(self):
        with allure.step('Кликнуть по кнопке "Личный кабинет"'):
            self.wait_and_click(self.driver, locator=self.locators.button_open_private_cabinet)

    def click_on_button_change_bread(self):
        with allure.step('Кликнуть по кнопке выбора булочки'):
            self.wait_and_click(self.driver, locator=self.locators.text_bread)

    def click_on_button_change_filling(self):
        with allure.step('Кликнуть по кнопке выбора начинки'):
            self.wait_and_click(self.driver, locator=self.locators.text_fillings)

    def click_on_button_change_sause(self):
        with allure.step('Кликнуть по кнопке выбора соуса'):
            self.wait_and_click(self.driver, locator=self.locators.text_sause)