import allure

from src import __locators
from utils.wait_er import wait_and_click, wait_and_send_keys, wait_for_url_contains


def click_on_button_private_cabinet(driver):
    with allure.step('Кликнуть по кнопке "Личный кабинет"'):
        wait_and_click(driver, locator=locators.button_private_cabinet)
        
def click_on_button_enter_to_account_on_main_page(driver):
    with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):    
        wait_and_click(driver, locator=locators.button_enter_to_account_on_main_page)
        
def click_on_button_restration_on_login_page(driver):
    with allure.step('Нажать на кнопку "Зарегистрироваться"'): 
        wait_and_click(driver, locator=locators.button_restration_on_login_page)
        
def input_registered_user_name(driver, username):
    with allure.step('Ввести имя регистрируемого пользователя'):
        wait_and_send_keys(driver, locator=locators.input_name_for_registration, value=username)

def input_registered_user_email(driver, email):
    with allure.step('Ввести email регистрируемого пользователя'):
        wait_and_send_keys(driver, locator=locators.input_email_for_registration, value=email)
        
def input_password(driver, password):
    with allure.step('Ввести пароль регистрируемого пользователя'):
        wait_and_send_keys(driver, locator=locators.input_password, value=password)

def click_on_button_registration_complete(driver):
    with allure.step('Кликнуть по кнопке "Зарегистрироваться"'):
        wait_and_click(driver, locator=locators.button_registration_complite)

def check_redirect_to_login_page(driver, expected_url):
    with allure.step('Проверить, что произошел редирект на страницу логина — регистрация успешна'):
        wait_for_url_contains(driver, expected_url=expected_url)
