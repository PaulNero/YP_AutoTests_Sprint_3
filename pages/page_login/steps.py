import allure

from .locators import PageLoginLocators
from ..base_page import BasePage

class PageLogin(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = PageLoginLocators

    def click_on_button_restration_on_login_page(self):
        with allure.step('Нажать на кнопку "Зарегистрироваться"'):
            self.wait_and_click(self.driver,
                                locator=self.locators.button_restration_on_login_page)

    def input_login_email(self, email):
        with allure.step('Ввести email пользователя'):
            self.wait_and_send_keys(self.driver,
                                    locator=self.locators.input_email_for_login,
                                    value=email)

    def input_login_password(self, password):
        with allure.step('Ввести пароль пользователя'):
            self.wait_and_send_keys(self.driver,
                                    locator=self.locators.input_password,
                                    value=password)

    def click_on_button_complete_login(self):
        with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):
            self.wait_and_click(self.driver,
                                locator=self.locators.button_complite_login)

    def click_on_button_forgot_password(self):
        with allure.step('Кликнуть по кнопке "Забыли пароль"'):
            self.wait_and_click(self.driver,
                                locator=self.locators.button_forgot_password)

    def check_redirect_to_login_page(self, expected_url):
        with allure.step('Проверить, что произошел редирект на страницу логина — регистрация успешна'):
            self.url_contains(self.driver, expected_url=expected_url)