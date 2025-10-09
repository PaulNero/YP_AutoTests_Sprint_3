from datetime import datetime
import pytest
import allure

from src import data
from src import links
from src import locators
from src.wait_er import wait_and_click, wait_and_send_keys, wait_for_url_contains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PageRegistration:
    def __init__(self, driver):
        self.driver = driver

    def click_on_button_private_cabinet(self):
        with allure.step('Кликнуть по кнопке "Личный кабинет"'):
            wait_and_click(self.driver, locator=locators.button_private_cabinet)


    def click_on_button_enter_to_account_on_main_page(self):
        with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):
            wait_and_click(self.driver, locator=locators.button_enter_to_account_on_main_page)


    def click_on_button_restration_on_login_page(self):
        with allure.step('Нажать на кнопку "Зарегистрироваться"'):
            wait_and_click(self.driver, locator=locators.button_restration_on_login_page)


    def input_registered_user_name(self, username):
        with allure.step('Ввести имя регистрируемого пользователя'):
            wait_and_send_keys(self.driver, locator=locators.input_name_for_registration, value=username)


    def input_registered_user_email(self, email):
        with allure.step('Ввести email регистрируемого пользователя'):
            wait_and_send_keys(self.driver, locator=locators.input_email_for_registration, value=email)


    def input_password(self, password):
        with allure.step('Ввести пароль регистрируемого пользователя'):
            wait_and_send_keys(self.driver, locator=locators.input_password, value=password)


    def click_on_button_registration_complete(self):
        with allure.step('Кликнуть по кнопке "Зарегистрироваться"'):
            wait_and_click(self.driver, locator=locators.button_registration_complite)


    def check_redirect_to_login_page(self, expected_url):
        with allure.step('Проверить, что произошел редирект на страницу логина — регистрация успешна'):
            wait_for_url_contains(self.driver, expected_url=expected_url)
