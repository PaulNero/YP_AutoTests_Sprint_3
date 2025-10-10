from selenium.webdriver.common.by import By

class HeaderLocators:
    button_private_cabinet = By.XPATH, '//nav/a[@href="/account"]' # Кнопка личный кабинет в хедере сайта
    button_open_constructor = By.XPATH, '//p[text()="Конструктор"]' # Кнопка конструктора в хедере сайта
    button_logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' # Кнопка лого в хедере сайта

