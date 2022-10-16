import pytest

from src import data
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.constructor_change
def test_constructor_parts_changed_to_bread(driver):
        driver.find_element(*locators.button_change_constructor_part_to_fillings).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_fillings))

        driver.find_element(*locators.button_change_constructor_part_to_bread).click()
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.text_bread))
        assert driver.find_element(*locators.text_bread).is_enabled()

@pytest.mark.constructor_change
def test_constructor_parts_changed_to_sause(driver):
        driver.find_element(*locators.button_change_constructor_part_to_fillings).click()
        WebDriverWait(driver, data.delay).until(
            EC.presence_of_element_located(locators.text_fillings))

        driver.find_element(*locators.button_change_constructor_part_to_sauce).click()
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.text_sause))

        assert driver.find_element(*locators.text_sause).is_enabled()

@pytest.mark.constructor_change
def test_constructor_parts_changed_to_filling(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_change_constructor_part_to_fillings)).click()
        WebDriverWait(driver, data.delay).until(
            EC.visibility_of_element_located(locators.text_fillings))

        assert driver.find_element(*locators.text_fillings).is_enabled()

