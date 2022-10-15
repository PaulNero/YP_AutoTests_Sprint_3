import pytest

from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.login
def test_login_page_via_private_cabinet_button(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_complite_login).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

@pytest.mark.login
def test_login_page_via_enter_account_button(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_complite_login).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

@pytest.mark.login
def test_login_page_via_registration(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_complite_login).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

@pytest.mark.login
def test_login_page_via_forgot_password(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_forgot_password)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        driver.find_element(*locators.input_password).send_keys(data.password_right)
        driver.find_element(*locators.button_complite_login).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
