
import pytest
import allure
from pages.page_registration.locators import PageRegistrationLocators
from src import data
from src import links
from src import __locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.setup_method import BaseUISteps

class TestPositivePageLogin(BaseUISteps):
    @allure.parent_suite('Логин')
    @pytest.mark.login
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Login')
    @allure.tag('smoke', 'regression')
    @pytest.mark.parametrize('entry_point, case_title',
                             [
                                ('private_cabinet', 'Логин через личный кабинет'),
                                ('enter_to_account', 'Логин через кнопку входа в аккаунт'),
                                ('enter_after_registration_form', 'Логин через форму регистрации'),
                                ('enter_after_forgot_password_form', 'Логин через страницу "Забыли пароль"')
                             ]
                             )
    def test_login_page_via_private_cabinet_button(self, driver, entry_point, case_title):
        allure.dynamic.title(case_title)

        if entry_point == 'private_cabinet':
            self.step_on_header.click_on_button_private_cabinet()
        elif entry_point == 'enter_to_account':
            self.step_on_constructor.click_on_button_enter_to_account_on_main_page()
        elif entry_point == 'enter_after_registration_form':
            self.step_on_header.click_on_button_private_cabinet()
            self.step_on_login.click_on_button_restration_on_login_page()
            self.step_on_registration.click_on_button_enter_to_account()
        elif entry_point == 'enter_after_forgot_password_form':
            self.step_on_header.click_on_button_private_cabinet()
            self.step_on_login.click_on_button_forgot_password()
            self.step_on_forgot_password.click_on_button_enter_to_account()

        self.step_on_login.input_login_email(value=data.email_for_login)
        self.step_on_login.input_login_password(value=data.password_right)
        self.step_on_login.click_on_button_complete_login()
        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_constructor.url_matches(driver,
                                                        expected_url=links.main_link
                                                        ), f'Произошла ошибка, текущая страница {driver.current_url}'

    @allure.parent_suite('Логин')
    @pytest.mark.login
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Login')
    @allure.tag('smoke', 'regression')
    @allure.title('Проверка авторизации только что созданным пользователем')
    def test_login_after_registration(self, driver, new_email):
        new_user = new_email

        self.step_on_header.click_on_button_private_cabinet()
        self.step_on_login.click_on_button_restration_on_login_page()
        self.step_on_registration.input_registered_user_name(username=data.name)
        self.step_on_registration.input_registered_user_email(email=new_user)
        self.step_on_registration.input_password(password=data.password_right)
        self.step_on_registration.click_on_button_registration_complete()
        self.step_on_login.check_redirect_to_login_page(expected_url=links.login_link)
        with allure.step('Проверить, что произошел корректный переход на страницу логина'):
            assert self.step_on_login.url_matches(driver, expected_url=links.main_link + links.login_link)

        self.step_on_login.input_login_email(value=new_user)
        self.step_on_login.input_login_password(value=data.password_right)
        self.step_on_login.click_on_button_complete_login()
        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_constructor.url_matches(driver,
                                                        expected_url=links.main_link
                                                        ), f'Произошла ошибка, текущая страница {driver.current_url}'
