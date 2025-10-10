import allure

# from src import locators
from .locators import PageForgotPasswordLocators
from ..base_page import BasePage


class PageRegistration(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = PageForgotPasswordLocators

    def click_on_button_enter_to_account(self):
        with allure.step('Кликнуть по кнопке "Войти"'):
            self.wait_and_click(self.driver,
                                locator=self.locators.button_enter_from_registr_of_fogot)
