from selenium.webdriver.common.by import By

class PageRegistrationLocators:
    button_eye_for_password = By.XPATH, '//*[contains(@d, "M12 ")]' # Кнопка глаза скрыть/показать пароль
    button_restration_on_login_page = By.XPATH, '//a[text()="Зарегистрироваться"]' # Кнопка перехода к форме регистрации с формы логина

    input_email_for_login = By.XPATH, '//input[@name="name"]' # Ввод email при логине
    input_password = By.XPATH, '//input[@name="Пароль"]' # Ввод пароля при логине
    input_name_for_registration = By.XPATH, '//fieldset[1]/div/div/input' # Ввод имени при регистрации
    input_email_for_registration = By.XPATH, '//fieldset[2]/div/div/input' # Ввод email при регистрации

    error_wrong_password = By.XPATH, '//p[text()="Некорректный пароль"]' # Ошибки принеправильном пароле при регистрации
    error_wrong_user_email = By.XPATH, '//p[text()="Такой пользователь уже существует"]' # Ошибка при регистрации пользователя


