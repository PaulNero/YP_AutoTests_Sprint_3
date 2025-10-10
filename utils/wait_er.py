from utils.decorators import with_error_handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src import data

class WaitMixin:

    @with_error_handling
    def wait_and_click(self, locator, timeout=None):
        delay = timeout or data.delay

        WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(locator)
                ).click()

    @with_error_handling
    def wait_and_send_keys(self, locator, value, timeout=None):
        delay = timeout or data.delay

        WebDriverWait(self.driver, delay).until(
            EC.visibility_of_element_located(locator)
                ).send_keys(value)


    # @with_error_handling
    # def wait_for_url_contains(self, expected_url, timeout=None):
    #     delay = timeout or data.delay
    #
    #     WebDriverWait(driver, delay).until(
    #         EC.url_contains(expected_url)
    #             )
