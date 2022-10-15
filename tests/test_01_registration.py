import pytest

from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

### Positive
@pytest.mark.registration
def test_registration_via_private_cabinet(new_email, driver):
        email = new_email
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        driver.find_element(*locators.input_email_for_registration).send_keys(email)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_registration_complite).click()

        WebDriverWait(driver, data.delay).until(EC.url_contains(links.login_link))
        assert driver.current_url == links.main_link + links.login_link

@pytest.mark.registration
def test_registration_via_button_enter_to_account(new_email, driver):
        email = new_email
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        driver.find_element(*locators.input_email_for_registration).send_keys(email)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_registration_complite).click()

        WebDriverWait(driver, data.delay).until(EC.url_contains(links.login_link))
        assert driver.current_url == links.main_link + links.login_link

### Negative
@pytest.mark.registration
def test_field_name_not_empty_failed_registration(new_email, driver):
        email = new_email
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_registration_complite).click()

        assert driver.current_url == links.main_link + links.register_link

@pytest.mark.registration
def test_wrong_password_error_failed_registration(new_email, driver):
        email = new_email

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        driver.find_element(*locators.input_email_for_registration).send_keys(email)
        driver.find_element(*locators.input_password).send_keys(data.password_wrong)
        driver.find_element(*locators.button_registration_complite).click()

        assert driver.find_element(*locators.error_wrong_password).is_displayed()

@pytest.mark.registration
def test_minimal_len_password_failed_registration(new_email, driver):
        email = new_email

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        driver.find_element(*locators.input_email_for_registration).send_keys(email)
        driver.find_element(*locators.input_password).send_keys(data.password_wrong)
        driver.find_element(*locators.button_registration_complite).click()

        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.error_wrong_password))

        assert driver.find_element(*locators.error_wrong_password).text == data.error_password_text

@pytest.mark.registration
def test_email_format_success_registration(new_email, driver):
        email = new_email

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        driver.find_element(*locators.input_email_for_registration).send_keys(email)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        get_email = driver.find_element(*locators.input_email_for_registration).get_attribute('value')
        driver.find_element(*locators.button_registration_complite).click()

        assert data.check_email(get_email) == True

@pytest.mark.registration
@pytest.mark.parametrize('case',
                         [("word"),
                          ("word@"),
                          ("word@word"),
                          ("word@word."),
                          ("@word"),
                          ("@word.word")])
def test_email_format_failed_registration(new_email, driver, case):

    WebDriverWait(driver, data.delay).until(
        EC.element_to_be_clickable(locators.button_private_cabinet)).click()
    WebDriverWait(driver, data.delay).until(
        EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

    WebDriverWait(driver, data.delay).until(
        EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
    driver.find_element(*locators.input_email_for_registration).send_keys(case)
    driver.find_element(*locators.input_password).send_keys(data.password_right)
    driver.find_element(*locators.button_registration_complite).click()

    WebDriverWait(driver, data.delay).until(
        EC.presence_of_element_located(locators.error_wrong_user_email))
    assert driver.find_element(*locators.error_wrong_user_email).text == data.error_user_text


