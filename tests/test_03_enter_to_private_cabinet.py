from src import driver_settings
from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_all_browsers():
    try:
        test_enter_private_cabinet_chrome_success()
        test_enter_private_cabinet_firefox_success()
        test_enter_private_cabinet_safari_success()
    except:
        pass

### Chrome
def test_enter_private_cabinet_chrome_success():
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

    except:
        driver.quit()

### Firefox
def test_enter_private_cabinet_firefox_success():
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

    except:
        driver.quit()

### Safari
def test_enter_private_cabinet_safari_success():
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

    except:
        driver.quit()