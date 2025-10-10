import allure
import pytest

from src import data
from src import links
from src import __locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.setup_method import BaseUISteps

class TestPositivePageLogin(BaseUISteps):

    @allure.parent_suite('Личный кабинет')
    @pytest.mark.private_cabinet
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Private Cabinet')
    @allure.tag('smoke', 'regression')
    @pytest.mark.parametrize('entry_point, case_title',
                             [
                                 ('header', 'Переход в личный кабинет через кнопку в хедере после авторизации'),
                                 ('page', 'Переход в личный кабинет через кнопку на сайте после авторизации')
                             ]
                             )
    def test_login_after_registration(self, driver, entry_point, case_title, new_email):
        allure.dynamic.title(case_title)
        new_user = new_email

        self.step_on_header.click_on_button_private_cabinet()
        self.step_on_login.click_on_button_restration_on_login_page()
        self.step_on_registration.input_registered_user_name(username=data.name)
        self.step_on_registration.input_registered_user_email(email=new_user)
        self.step_on_registration.input_password(password=data.password_right)
        self.step_on_registration.click_on_button_registration_complete()
        self.step_on_login.check_redirect_to_login_page(expected_url=links.login_link)
        with allure.step('Проверить, что произошел корректный переход на страницу логина'):
            assert self.step_on_login.url_matches(driver,
                                                  expected_url=links.main_link + links.login_link
                                                  ), f'Произошла ошибка, текущая страница {driver.current_url}'

        self.step_on_login.input_login_email(value=new_user)
        self.step_on_login.input_login_password(value=data.password_right)
        self.step_on_login.click_on_button_complete_login()
        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_constructor.url_matches(driver,
                                                        expected_url=links.main_link
                                                        ), f'Произошла ошибка, текущая страница {driver.current_url}'

        if entry_point == 'header':
            self.step_on_header.click_on_button_private_cabinet()
        elif entry_point == 'page':
            self.step_on_constructor.click_on_button_private_cabinet()

        with allure.step('Проверить, что произошел корректный переход в личный кабинет'):
            assert self.step_on_private_cabinet.url_contains(driver,
                                                             expected_url=links.private_cabinet
                                                             ), f'Произошла ошибка, текущая страница {driver.current_url}'

    @allure.parent_suite('Личный кабинет')
    @pytest.mark.private_cabinet
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Private Cabinet')
    @allure.tag('smoke', 'regression')
    @pytest.mark.parametrize('entry_point, case_title',
                             [
                                 ('header', 'Переход в личный кабинет через кнопку в хедере после авторизации'),
                                 ('page', 'Переход в личный кабинет через кнопку на сайте после авторизации')
                             ]
                             )
    def test_exit_from_account(self, driver):

        self.step_on_header.click_on_button_private_cabinet()
        self.step_on_login.check_redirect_to_login_page(expected_url=links.login_link)
        self.step_on_login.input_login_email(value=data.email_for_login)
        self.step_on_login.input_login_password(value=data.password_right)
        self.step_on_login.click_on_button_complete_login()
        self.step_on_header.click_on_button_private_cabinet()
        with allure.step('Проверить, что произошел корректный переход в личный кабинет'):
            assert self.step_on_private_cabinet.url_contains(driver,
                                                             expected_url=links.private_cabinet
                                                             ), f'Произошла ошибка, текущая страница {driver.current_url}'
        self.step_on_private_cabinet.click_on_button_exit()
        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_private_cabinet.url_contains(driver,
                                                             expected_url=links.main_link
                                                             ), f'Произошла ошибка, текущая страница {driver.current_url}'
