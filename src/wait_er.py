import allure
from src.decorators import with_error_handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from allure_commons.types import AttachmentType
from src.utils import attach_screenshot_and_log

from src import data

@with_error_handling
def wait_and_click(driver, locator, timeout=None):
    delay = timeout or data.delay
    
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(locator)
            ).click()
            
@with_error_handling      
def wait_and_send_keys(driver, locator, value, timeout=None):
    delay = timeout or data.delay
    
    WebDriverWait(driver, delay).until(
        EC.visibility_of_element_located(locator)
            ).send_keys(value)
        

@with_error_handling
def wait_for_url_contains(driver, expected_url, timeout=None):
    delay = timeout or data.delay
    
    WebDriverWait(driver, delay).until(
        EC.url_contains(expected_url)
            )
