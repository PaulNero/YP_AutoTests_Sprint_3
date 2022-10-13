import pytest

from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

### Positive
@pytest.mark.all
@pytest.mark.registration
def test_registration_via_private_cabinet_chrome_success(new_email, driver):
        email = new_email
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()
        WebDriverWait(driver, data.delay).until(EC.url_contains(links.login_link))

        assert driver.current_url == links.main_link + links.login_link

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

@pytest.mark.all
@pytest.mark.registration
def test_registration_via_button_enter_to_account_chrome_success(new_email, driver):
        email = new_email
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()
        WebDriverWait(driver, data.delay).until(EC.url_contains(links.login_link))

        assert driver.current_url == links.main_link + links.login_link

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

### Negative
@pytest.mark.all
@pytest.mark.registration
def test_field_name_not_empty_chrome_failed_registration(new_email, driver):
        email = new_email
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()

        assert driver.current_url == links.main_link + links.register_link
        assert not driver.find_element(*locators.button_registration_complite).click()

@pytest.mark.all
@pytest.mark.registration
def test_wrong_password_error_chrome_failed_registration(new_email, driver):
        email = new_email

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_wrong)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()

        assert driver.find_element(*locators.error_wrong_password).is_displayed()

@pytest.mark.all
@pytest.mark.registration
def test_minimal_len_password_chrome_failed_registration(new_email, driver):
        email = new_email

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_wrong)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.error_wrong_password))

        assert driver.find_element(*locators.error_wrong_password).text == data.error_password_text

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).clear()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_6_symbols)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()

        WebDriverWait(driver, data.delay).until(EC.url_contains(links.login_link))
        assert driver.current_url == links.main_link + links.login_link

@pytest.mark.all
@pytest.mark.registration
def test_email_format_chrome_failed_registration(new_email, driver):
        email = new_email
        wrong_email_cases = data.wrong_email_cases()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_name_for_registration)).send_keys(data.name)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)

        for check_email in wrong_email_cases:
            WebDriverWait(driver, data.delay).until(
                EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(check_email)
            WebDriverWait(driver, data.delay).until(
                EC.element_to_be_clickable(locators.button_registration_complite)).click()
            WebDriverWait(driver, data.delay).until(
                EC.presence_of_element_located(locators.error_wrong_user_email))
            assert driver.find_element(*locators.error_wrong_user_email).text == data.error_user_text
            WebDriverWait(driver, data.delay).until(
                EC.visibility_of_element_located(
                    locators.input_email_for_registration)).send_keys(Keys.SHIFT + Keys.UP, Keys.BACKSPACE)

        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.input_email_for_registration)).send_keys(email)
        get_email = driver.find_element(*locators.input_email_for_registration).get_attribute('value')
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_registration_complite)).click()

        assert data.check_email(get_email) == True
