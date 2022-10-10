from src import driver_settings
from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_all_browsers():
    try:
        test_enter_constructor_from_cabinet_via_constructor_button_chrome_success()
        test_enter_constructor_from_cabinet_via_constructor_button_firefox_success()
        test_enter_constructor_from_cabinet_via_constructor_button_safari_success()
    except:
        pass

def test_enter_constructor_from_cabinet_via_constructor_button_chrome_success():
    try:
        driver = driver_settings.chrome_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_private_cabinet)).click()

        assert driver.current_url == links.main_link + links.private_cabinet

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_constructor_constructor)).click()

        assert driver.current_url == links.main_link + links.constructor

    except:
        driver.quit()

def test_enter_constructor_from_cabinet_via_constructor_button_firefox_success():
    try:
        driver = driver_settings.firefox_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_private_cabinet)).click()

        assert driver.current_url == links.main_link + links.private_cabinet

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_constructor)).click()

        assert driver.current_url == links.main_link + links.constructor

    except:
        driver.quit()

def test_enter_constructor_from_cabinet_via_constructor_button_safari_success():
    try:
        driver = driver_settings.safari_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_private_cabinet)).click()

        assert driver.current_url == links.main_link + links.private_cabinet

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_constructor)).click()

        assert driver.current_url == links.main_link + links.constructor

    except:
        driver.quit()