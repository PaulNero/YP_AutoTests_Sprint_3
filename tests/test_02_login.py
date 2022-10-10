from src import driver_settings
from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_all_browsers():
    try:
        test_login_page_via_private_cabinet_button_chrome_success()
        test_login_page_via_enter_account_button_chrome_success()
        test_login_page_via_registration_chrome_success()
        test_login_page_via_forgot_password_chrome_success()

        test_login_page_via_private_cabinet_button_firefox_success()
        test_login_page_via_enter_account_button_firefox_success()
        test_login_page_via_registration_firefox_success()
        test_login_page_via_forgot_password_firefox_success()

        test_login_page_via_private_cabinet_button_safari_success()
        test_login_page_via_enter_account_button_safari_success()
        test_login_page_via_registration_safari_success()
        test_login_page_via_forgot_password_safari_success()
    except:
        pass

### Chrome
def test_login_page_via_private_cabinet_button_chrome_success():
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
    except:
        driver.quit()

def test_login_page_via_enter_account_button_chrome_success():
    try:
        driver = driver_settings.chrome_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

def test_login_page_via_registration_chrome_success():
    try:
        driver = driver_settings.chrome_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

def test_login_page_via_forgot_password_chrome_success():
    try:
        driver = driver_settings.chrome_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_forgot_password)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

### Firefox
def test_login_page_via_private_cabinet_button_firefox_success():
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
    except:
        driver.quit()

def test_login_page_via_enter_account_button_firefox_success():
    try:
        driver = driver_settings.firefox_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

def test_login_page_via_registration_firefox_success():
    try:
        driver = driver_settings.firefox_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

def test_login_page_via_forgot_password_firefox_success():
    try:
        driver = driver_settings.firefox_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_forgot_password)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

### Safari
def test_login_page_via_private_cabinet_button_safari_success():
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
    except:
        driver.quit()

def test_login_page_via_enter_account_button_safari_success():
    try:
        driver = driver_settings.safari_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

def test_login_page_via_registration_safari_success():
    try:
        driver = driver_settings.safari_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_restration_on_login_page)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()

def test_login_page_via_forgot_password_safari_success():
    try:
        driver = driver_settings.safari_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_to_account_on_main_page)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_forgot_password)).click()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_enter_from_registr_of_fogot)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link
    except:
        driver.quit()