import allure

# from src import locators
from .locators import PageRegistrationLocators
from ..base_page import BasePage


class PageRegistration(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = PageRegistrationLocators

    def input_registered_user_name(self, username):
        with allure.step('Ввести имя регистрируемого пользователя'):
            self.wait_and_send_keys(self.driver,
                                    locator=self.locators.input_name_for_registration,
                                    value=username)


    def input_registered_user_email(self, email):
        with allure.step('Ввести email регистрируемого пользователя'):
            self.wait_and_send_keys(self.driver,
                                    locator=self.locators.input_email_for_registration,
                                    value=email)


    def input_password(self, password):
        with allure.step('Ввести пароль регистрируемого пользователя'):
            self.wait_and_send_keys(self.driver,
                                    locator=self.locators.input_password,
                                    value=password)

    def click_on_button_enter_to_account(self):
        with allure.step('Кликнуть по кнопке "Войти"'):
            self.wait_and_click(self.driver,
                                locator=self.locators.button_enter_from_registr_of_fogot)


    def click_on_button_registration_complete(self):
        with allure.step('Кликнуть по кнопке "Зарегистрироваться"'):
            self.wait_and_click(self.driver,
                                locator=self.locators.button_registration_complite)

