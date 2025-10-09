from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    button_enter_to_account_on_main_page = By.XPATH, '//button[text()="Войти в аккаунт"]'  # Кнопка войти в аккаунт на главной странице
    button_change_constructor_part_to_bread = By.XPATH, '//span[text()="Булки"]' # Кнопка перехода к разделу булки в конструкторе
    button_change_constructor_part_to_sauce = By.XPATH, '//span[text()="Соусы"]' # Кнопка перехода к разделу соусы в конструкторе
    button_change_constructor_part_to_fillings = By.XPATH, '//span[text()="Начинки"]' # Кнопка перехода к разделу начинки в конструкторе

    text_fillings = By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]' # Контрольное название начинки 6 тест
    text_sause = By.XPATH, '//p[text()="Соус Spicy-X"]' # Контрольное название соуса 6 тест
    text_bread = By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]' # Контрольное название хлеба 6 тест
