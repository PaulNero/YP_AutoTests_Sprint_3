import pytest
import allure

from src import data
from src import links
from src import __locators
from pages.page_constructor.locators import ConstructorPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.setup_method import BaseUISteps

class TestPageRegistration(BaseUISteps):
    @allure.parent_suite('Конструктор')
    @pytest.mark.constructor
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Constructor')
    @allure.tag('smoke', 'regression')
    @allure.title('Проверка переходов на конструктор через логотип и кнопку в хедере')
    def test_enter_constructor_from_cabinet_via_constructor_button(self, driver):

        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_private_cabinet.url_contains(driver,
                                                             expected_url=links.main_link
                                                             ), f'Произошла ошибка, текущая страница {driver.current_url}'


        self.step_on_header.click_on_button_private_cabinet()
        self.step_on_login.input_login_email(data.email_for_login)
        self.step_on_login.input_login_password(data.password_right)
        self.step_on_login.click_on_button_complete_login()

        self.step_on_header.click_on_button_private_cabinet()
        self.step_on_header.click_on_button_logo()

        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_header.url_matches(driver,
                                                    expected_url=links.main_link
                                                    ), f'Произошла ошибка, текущая страница {driver.current_url}'

        self.step_on_header.click_on_button_private_cabinet()
        self.step_on_header.click_on_button_constructor()

        with allure.step('Проверить, что произошел корректный переход на главную страницу'):
            assert self.step_on_header.url_matches(driver,
                                                    expected_url=links.main_link
                                                    ), f'Произошла ошибка, текущая страница {driver.current_url}'

    @allure.parent_suite('Конструктор')
    @pytest.mark.constructor
    @pytest.mark.positive
    @allure.suite('Позитивные сценарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('component', 'Constructor')
    @allure.tag('smoke', 'regression')
    @allure.title('Проверка переключения ингридиентов при собирании бургера')
    def test_constructor_parts_change(self, driver):
        self.step_on_constructor.click_on_button_change_sause()
        assert self.step_on_constructor.visibility_element(driver, locator=ConstructorPageLocators.text_sause)

        self.step_on_constructor.click_on_button_change_filling()
        assert self.step_on_constructor.visibility_element(driver, locator=ConstructorPageLocators.text_fillings)

        self.step_on_constructor.click_on_button_change_bread()
        assert self.step_on_constructor.visibility_element(driver, locator=ConstructorPageLocators.text_bread)

    # @pytest.mark.constructor_change
    # def test_constructor_parts_changed_to_bread(driver):
    #         driver.find_element(*locators.button_change_constructor_part_to_fillings).click()
    #         WebDriverWait(driver, data.delay).until(
    #             EC.presence_of_element_located(locators.text_fillings))
    #
    #         driver.find_element(*locators.button_change_constructor_part_to_bread).click()
    #         WebDriverWait(driver, data.delay).until(
    #             EC.visibility_of_element_located(locators.text_bread))
    #         assert driver.find_element(*locators.text_bread).is_enabled()
    #
    # @pytest.mark.constructor_change
    # def test_constructor_parts_changed_to_sause(driver):
    #         driver.find_element(*locators.button_change_constructor_part_to_fillings).click()
    #         WebDriverWait(driver, data.delay).until(
    #             EC.presence_of_element_located(locators.text_fillings))
    #
    #         driver.find_element(*locators.button_change_constructor_part_to_sauce).click()
    #         WebDriverWait(driver, data.delay).until(
    #             EC.visibility_of_element_located(locators.text_sause))
    #
    #         assert driver.find_element(*locators.text_sause).is_enabled()
    #
    # @pytest.mark.constructor_change
    # def test_constructor_parts_changed_to_filling(driver):
    #         WebDriverWait(driver, data.delay).until(
    #             EC.element_to_be_clickable(locators.button_change_constructor_part_to_fillings)).click()
    #         WebDriverWait(driver, data.delay).until(
    #             EC.visibility_of_element_located(locators.text_fillings))
    #
    #         assert driver.find_element(*locators.text_fillings).is_enabled()