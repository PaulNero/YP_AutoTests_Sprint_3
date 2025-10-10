import pytest
import allure

from pages.base_page import BasePage
from pages.page_constructor.steps import PageConstructor
from pages.page_login.steps import PageLogin
from pages.page_header.steps import PageHeader
from pages.page_private_cabinet.steps import PagePrivateCabinet
from pages.page_registration.steps import PageRegistration
from pages.page_forgot_password.steps import PageForgotPasswordLocators

class BaseUISteps(BasePage):
    def setup_method(self, method, driver):
        self.driver = driver
        self.step_on_constructor = PageConstructor(driver)
        self.step_on_login = PageLogin(driver)
        self.step_on_registration = PageRegistration(driver)
        self.step_on_header = PageHeader(driver)
        self.step_on_private_cabinet = PagePrivateCabinet(driver)
        self.step_on_forgot_password = PageForgotPasswordLocators(driver)