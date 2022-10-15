import pytest

from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.open_constructor
def test_enter_constructor_from_cabinet_via_constructor_button(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_complite_login).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.url_contains(links.private_cabinet))

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_constructor)).click()
        WebDriverWait(driver, data.delay).until(
            EC.url_contains(links.main_link))

        assert driver.current_url == links.main_link
