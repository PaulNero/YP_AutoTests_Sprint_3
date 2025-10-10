from importlib.metadata import entry_points

import pytest
import allure

from pages.page_registration.steps import PageRegistration
from pages.page_registration.locators import PageRegistrationLocators
from pages.page_constructor.steps import PageConstructor
from pages.page_login.steps import PageLogin
from pages.page_header.steps import PageHeader
from src import data
from src import links
# from src import locators
# from src import steps
from utils import assertion, utils, setup_method

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.setup_method import BaseUISteps


class TestPageRegistration(BaseUISteps):

    @allure.parent_suite('Регистрация')
    @pytest.mark.registration
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Registration')
    @allure.tag('smoke', 'regression')
    @pytest.mark.parametrize('entry_point, case_title',
                             [
                                 ('private_cabinet', 'Регистрация через личный кабинет'),
                                 ('enter_to_account', 'Регистрация через кнопку входа в аккаунт')
                             ]
    )
    def test_registration_via_private_cabinet(self, driver, entry_point, case_title, new_email):
            allure.dynamic.title(case_title)

            # Параметризированные шаги
            if entry_point == 'private_cabinet':
                self.step_on_header.click_on_button_private_cabinet()
            elif entry_point == 'enter_to_account':
                self.step_on_constructor.click_on_button_enter_to_account_on_main_page()

            self.step_on_login.click_on_button_restration_on_login_page()
            self.step_on_registration.input_registered_user_name(username=data.name)
            self.step_on_registration.input_registered_user_email(email=new_email)
    
            get_email = self.step_on_registration.find_element(driver,
                                               locator=PageRegistrationLocators.input_email_for_registration
                                               ).get_attribute('value')
            assert utils.check_email(get_email) == True
    
            self.step_on_registration.input_password(password=data.password_right)
            self.step_on_registration.click_on_button_registration_complete()
            self.step_on_login.check_redirect_to_login_page(expected_url=links.login_link)
            assert self.step_on_login.url_matches(driver,
                                                  expected_url=links.main_link + links.login_link
                                                  ), f'Произошла ошибка, текущая страница {driver.current_url}'
        
    @allure.parent_suite('Регистрация')
    @pytest.mark.registration
    @pytest.mark.negative
    @allure.suite('Негативные сценарии')
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('component', 'Registration')
    @allure.tag('regression')
    @pytest.mark.parametrize('input_value_type, description, case_title',
                                [
                                    ('email', 'Не заполняем Имя', 'Проверка регистрации без заполнения Имени пользователя'),
                                    ('name', 'Не заполняем Email', 'Проверка регистрации без заполнения Email пользователя')
                                ]
                            )
    def test_field_name_not_empty_failed_registration(self, driver, input_value_type, description, case_title, new_email):
        allure.dynamic.title(case_title)
        
        self.step_on_constructor.click_on_button_enter_to_account_on_main_page()
        self.step_on_login.click_on_button_restration_on_login_page()

        # Параметризированные шаги
        with allure.step(description):
            if input_value_type == 'email':
                self.step_on_registration.input_registered_user_name(username=data.name)
            elif input_value_type == 'name':
                self.step_on_registration.input_registered_user_email(email=new_email)
            
        self.step_on_registration.input_password(password=data.password_right)
        
        # Сохраняем текущий URL, что бы проверить его ниже, после нажатия кнопки регистрации
        current_url = driver.current_url
        
        self.step_on_registration.click_on_button_registration_complete()
        
        with allure.step('Проверить, что редирект на страницу логина не произошел — регистрация провалена, ошибок нет'):
            self.step_on_registration.url_not_changed(current_url = current_url
                                                      ), f'Произошла ошибка, текущая страница {driver.current_url}'
    
    @allure.parent_suite('Регистрация')
    @pytest.mark.registration
    @pytest.mark.negative
    @allure.suite('Негативные сценарии')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label('component', 'Registration')
    @allure.tag('regression')
    @allure.title('Проверить, что система не принимает пароли короче 6-ти символов')
    def test_wrong_lenght_password_error_failed_registration(self, driver):
        
        self.step_on_constructor.click_on_button_enter_to_account_on_main_page()
        self.step_on_login.click_on_button_restration_on_login_page()
        self.step_on_registration.input_password(password=data.password_wrong)
        self.step_on_registration.click_on_button_registration_complete()
        
        with allure.step(f'Проверить, что появилась ошибка "{data.error_password_text}"'):
            error = self.step_on_registration.find_element(driver, PageRegistrationLocators.error_wrong_password)
            assert error.is_displayed()
            assert error.text == data.error_password_text
            
        self.step_on_registration.input_password(password=data.password_6_symbols)
        self.step_on_registration.click_on_button_registration_complete()
    
        with allure.step(f'Проверить, что исчезла ошибка "{data.error_password_text}"'):
            assert self.step_on_registration.invisibility_element(driver, locator=PageRegistrationLocators.error_wrong_password
                                                  ), f'Ошибка "{data.error_password_text}" не исчезла с экрана'
    
    @allure.parent_suite('Регистрация')
    @pytest.mark.registration
    @pytest.mark.negative
    @allure.suite('Негативные сценарии')
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('component', 'Registration')
    @allure.tag('regression')
    @pytest.mark.parametrize('case',
                            [("word"),
                            ("word@"),
                            ("word@word"),
                            ("word@word."),
                            ("@word"),
                            ("@word.word")])
    def test_email_format_failed_registration(self, driver, case):
        allure.dynamic.title(f'Система корректно реагирует на неправильный формат Email: {case}')

        self.step_on_constructor.click_on_button_enter_to_account_on_main_page()
        self.step_on_login.click_on_button_restration_on_login_page()
        self.step_on_registration.input_registered_user_name(username=data.name)
        self.step_on_registration.input_registered_user_email(email=case)
        
        get_email = self.step_on_registration.find_element(driver,
                                           locator=PageRegistrationLocators.input_email_for_registration
                                           ).get_attribute('value')
        assert utils.check_email(get_email) == False
        
        self.step_on_registration.input_password(password=data.password_right)
        self.step_on_registration.click_on_button_registration_complete()
    
        with allure.step(f'Проверить, что при невалидном Email отображается ошибка "{data.error_user_text}"'):
            assert self.step_on_registration.find_element(driver,
                                          locator=PageRegistrationLocators.error_wrong_user_email
                                          ).text == data.error_user_text
            

