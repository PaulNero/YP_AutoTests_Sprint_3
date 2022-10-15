import pytest

from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.enter_to_cabinet
def test_enter_private_cabinet(driver):
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

        assert driver.current_url == links.main_link + links.private_cabinet
