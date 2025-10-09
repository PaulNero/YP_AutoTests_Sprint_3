from datetime import datetime
import pytest
import allure
import time

from src import data
from src import links
from src import locators
from src import steps
from src import assertion
from src import utils
# from pages.page_registration import steps, locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.parent_suite('Регистрация')
@pytest.mark.registration
@pytest.mark.positive
@allure.suite('Позитивные сценарии')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('component', 'Registration')
@allure.tag('smoke', 'regression')

@pytest.mark.parametrize('action, case_title',
                            [
                                (steps.click_on_button_private_cabinet, 'Регистрация через личный кабинет'),
                                (steps.click_on_button_enter_to_account_on_main_page, 'Регистрация через кнопку входа в аккаунт')
                            ]
                        )
def test_registration_via_private_cabinet(driver, action, case_title, new_email):
    
    allure.dynamic.title(case_title)
    
    action(driver) # Параметризированные шаги
    
    steps.click_on_button_restration_on_login_page(driver)
    steps.input_registered_user_name(driver, username=data.name)
    steps.input_registered_user_email(driver, email=new_email)
    
    get_email = assertion.find_element(driver, 
                                            locator=locators.input_email_for_registration
                                            ).get_attribute('value')
    
    assert utils.check_email(get_email) == True
    
    steps.input_password(driver, password=data.password_right)
    steps.click_on_button_registration_complete(driver)
    steps.check_redirect_to_login_page(driver, expected_url=links.login_link)
    assert assertion.url_matches(driver, expected_url=links.main_link + links.login_link)
    
@allure.parent_suite('Регистрация')
@pytest.mark.registration
@pytest.mark.negative
@allure.suite('Негативные сценарии')
@allure.severity(allure.severity_level.MINOR)
@allure.label('component', 'Registration')
@allure.tag('regression')
@pytest.mark.parametrize('input_locator, input_value_type, description, case_title',
                            [
                                (locators.input_email_for_registration, 'email', 'Ввести email, не вводить Имя', 'Проверка регистрации без заполнения Имени пользователя'),
                                (locators.input_name_for_registration, 'name', 'Ввести имя, не вводить email', 'Проверка регистрации без заполнения Email пользователя')
                            ]
                        )
def test_field_name_not_empty_failed_registration(driver, input_locator, input_value_type, description, case_title, new_email):
    allure.dynamic.title(case_title)
    
    input_value = new_email if input_value_type == 'email' else data.name
    
    steps.click_on_button_enter_to_account_on_main_page(driver)
    steps.click_on_button_restration_on_login_page(driver)
    
    with allure.step(description):
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(input_locator)).send_keys(input_value)
        
    steps.input_password(driver, password=data.password_right)
    
    # Сохраняем текущий URL, что бы проверить его ниже, после нажатия кнопки регистрации
    current_url = driver.current_url
    
    steps.click_on_button_registration_complete(driver)
    
    with allure.step('Проверить, что редирект на страницу логина не произошел — регистрация провалена, ошибок нет'):
        assertion.url_not_changed(driver, current_url = current_url)

@allure.parent_suite('Регистрация')
@pytest.mark.registration
@pytest.mark.negative
@allure.suite('Негативные сценарии')
@allure.severity(allure.severity_level.NORMAL)
@allure.label('component', 'Registration')
@allure.tag('regression')
@allure.title('Проверить, что система не принимает пароли короче 6-ти символов')
def test_wrong_lenght_password_error_failed_registration(driver):
    
    steps.click_on_button_enter_to_account_on_main_page(driver)
    steps.click_on_button_restration_on_login_page(driver)
    steps.input_password(driver, password=data.password_wrong)
    steps.click_on_button_registration_complete(driver)
    
    with allure.step(f'Проверить, что появилась ошибка "{data.error_password_text}"'):
        
        error = assertion.find_element(driver, locators.error_wrong_password)
        assert error.is_displayed()
        assert error.text == data.error_password_text
        
    steps.input_password(driver, password=data.password_6_symbols)
    steps.click_on_button_registration_complete(driver)

    with allure.step(f'Проверить, что исчезла ошибка "{data.error_password_text}"'):
        
        assert assertion.invisibility_element(driver, locator=locators.error_wrong_password
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
def test_email_format_failed_registration(driver, case):
    allure.dynamic.title(f'Система корректно реагирует на неправильный формат Email: {case}')

    steps.click_on_button_enter_to_account_on_main_page(driver)
    steps.click_on_button_restration_on_login_page(driver)
    steps.input_registered_user_name(driver, username=data.name)
    steps.input_registered_user_email(driver, email=case)
    
    get_email = assertion.find_element(driver, 
                                            locator=locators.input_email_for_registration
                                            ).get_attribute('value')
    assert utils.check_email(get_email) == False
    
    steps.input_password(driver, password=data.password_right)
    steps.click_on_button_registration_complete(driver)

    with allure.step(f'Проверить, что при невалидном Email отображается ошибка "{data.error_user_text}"'):
        assert assertion.find_element(driver, 
                                    locator=locators.error_wrong_user_email
                                    ).text == data.error_user_text
        

