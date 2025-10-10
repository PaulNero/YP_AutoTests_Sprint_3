from utils.decorators import with_error_handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from src import data

class AssertionMixin:

    @with_error_handling
    def visibility_element(self, locator, timeout=None):
        delay = timeout or data.delay

        return WebDriverWait(self.driver, delay).until(
            EC.visibility_of_element_located(locator)
        )

    @with_error_handling
    def invisibility_element(self, locator, timeout=None):
        delay = timeout or data.delay

        return WebDriverWait(self.driver, delay).until(
            EC.invisibility_of_element_located(locator)
        )

    @with_error_handling
    def find_element(self, locator, timeout=None):
        delay = timeout or data.delay

        return WebDriverWait(self.driver, delay).until(
            EC.presence_of_element_located(locator)
        )

    @with_error_handling
    def url_matches(self, expected_url, timeout=None):
        delay = timeout or data.delay

        return WebDriverWait(self.driver, delay).until(
            EC.url_to_be(expected_url)
        )

    @with_error_handling
    def url_contains(self, expected_url, timeout=None):
        delay = timeout or data.delay

        return WebDriverWait(self.driver, delay).until(
            EC.url_contains(expected_url)
        )

    @with_error_handling
    def url_not_changed(self, current_url, timeout=None):
        delay = timeout or data.delay
        try:
            WebDriverWait(self.driver, delay).until(lambda d: d.current_url == current_url)
        except TimeoutException:
            raise AssertionError(f'URL изменился: ожидался {current_url}, стал {self.driver.current_url}')