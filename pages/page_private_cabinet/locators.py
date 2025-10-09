from selenium.webdriver.common.by import By

class PagePrivateCabinetLocators:
    button_private_cabinet = By.XPATH, '//nav/a[@href="/account"]' # Кнопка личный кабинет в хедере сайта
    button_open_private_cabinet = By.XPATH, '//p[text()="Личный Кабинет"]' # Кнопка личный кабинет после логина
    button_exit_from_account = By.XPATH, '//button[text()="Выход"]' # Кнопка выход в личном кабинете
