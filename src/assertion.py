import allure
from src.decorators import with_error_handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from src.utils import attach_screenshot_and_log

from src import data

@with_error_handling
def visibility_element(driver, locator, timeout=None):
    delay = timeout or data.delay
    
    return WebDriverWait(driver, delay).until(
        EC.visibility_of_element_located(locator)
    )
    
@with_error_handling
def invisibility_element(driver, locator, timeout=None):
    delay = timeout or data.delay
    
    return WebDriverWait(driver, delay).until(
        EC.invisibility_of_element_located(locator)
    )
    
@with_error_handling
def find_element(driver, locator, timeout=None):
    delay = timeout or data.delay
    
    return WebDriverWait(driver, delay).until(
        EC.presence_of_element_located(locator)
    )

@with_error_handling
def url_matches(driver, expected_url, timeout=None):
    delay = timeout or data.delay
    
    return WebDriverWait(driver, delay).until(
        EC.url_to_be(expected_url)
    )

@with_error_handling
def url_contains(driver, expected_url, timeout=None):
    delay = timeout or data.delay
    
    return WebDriverWait(driver, delay).until(
        EC.url_contains(expected_url)
    )

@with_error_handling
def url_not_changed(driver, current_url, timeout=None):
    delay = timeout or data.delay
    try:
        WebDriverWait(driver, delay).until(lambda d: d.current_url == current_url)
    except TimeoutException:
        raise AssertionError(f'URL изменился: ожидался {current_url}, стал {driver.current_url}')