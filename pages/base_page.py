import allure
from utils import wait_er
# from utils.wait_er import wait_and_click, wait_and_send_keys
from utils.assertion import AssertionMixin
from utils.wait_er import WaitMixin

class BasePage(AssertionMixin, WaitMixin):
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, description=None):
        step_text = description or f'Клик по элементу {locator}'
        with allure.step(step_text):
            WaitMixin.wait_and_click(self.driver, locator)

    def input_text(self, locator, value, description=None):
        step_text = description or f'Ввод текста "{value}" в элемент {locator}'
        with allure.step(step_text):
            WaitMixin.wait_and_send_keys(self.driver, locator, value)

