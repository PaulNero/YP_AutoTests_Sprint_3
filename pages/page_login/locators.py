from selenium.webdriver.common.by import By

class PageLoginLocators:
    button_complite_login = By.XPATH, '//button[text()="Войти"]' # Кнопка завершения входа после ввода данных
    button_eye_for_password = By.XPATH, '//*[contains(@d, "M12 ")]' # Кнопка глаза скрыть/показать пароль
    button_restration_on_login_page = By.XPATH, '//a[text()="Зарегистрироваться"]' # Кнопка перехода к форме регистрации с формы логина
    button_forgot_password = By.XPATH, '//a[@href="/forgot-password"]' # Кнопка перехода к форме забыли пароль с формы логина
    input_email_for_login = By.XPATH, '//input[@name="name"]' # Ввод email при логине
    input_password = By.XPATH, '//input[@name="Пароль"]' # Ввод пароля при логине

