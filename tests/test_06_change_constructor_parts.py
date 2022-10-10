from src import driver_settings
from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_all_browsers():
    test_change_constructor_parts_chrome_parts_changed()
    test_change_constructor_parts_firefox_parts_changed()
    test_change_constructor_parts_safari_parts_changed()

def test_change_constructor_parts_chrome_parts_changed():
    try:
        driver = driver_settings.chrome_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_fillings)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_fillings))

        assert driver.find_element(*locators.text_fillings).is_enabled()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_sauce)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_sause))

        assert driver.find_element(*locators.text_sause).is_enabled()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_bread)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_bread))

        assert driver.find_element(*locators.text_bread).is_enabled()

    except:
        driver.quit()

def test_change_constructor_parts_firefox_parts_changed():
    try:
        driver = driver_settings.firefox_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_fillings)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_fillings))

        assert driver.find_element(*locators.text_fillings).is_enabled()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_sauce)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_sause))

        assert driver.find_element(*locators.text_sause).is_enabled()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_bread)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_bread))

        assert driver.find_element(*locators.text_bread).is_enabled()

    except:
        driver.quit()

def test_change_constructor_parts_safari_parts_changed():
    try:
        driver = driver_settings.safari_browser()
        driver.get(links.main_link)

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_fillings)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_fillings))

        assert driver.find_element(*locators.text_fillings).is_enabled()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_sauce)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_sause))

        assert driver.find_element(*locators.text_sause).is_enabled()

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_bread)).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_bread))

        assert driver.find_element(*locators.text_bread).is_enabled()

    except:
        driver.quit()