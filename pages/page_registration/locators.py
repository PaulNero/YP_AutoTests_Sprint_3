from selenium.webdriver.common.by import By

class PageRegistrationLocators:
    button_eye_for_password = By.XPATH, '//*[contains(@d, "M12 ")]' # Кнопка глаза скрыть/показать пароль

    input_name_for_registration = By.XPATH, '//fieldset[1]/div/div/input' # Ввод имени при регистрации
    input_email_for_registration = By.XPATH, '//fieldset[2]/div/div/input' # Ввод email при регистрации
    input_password = By.XPATH, '//input[@name="Пароль"]'  # Ввод пароля при логине

    error_wrong_password = By.XPATH, '//p[text()="Некорректный пароль"]' # Ошибки при неправильном пароле при регистрации
    error_wrong_user_email = By.XPATH, '//p[text()="Такой пользователь уже существует"]' # Ошибка при регистрации пользователя

    button_registration_complite = By.XPATH, '//button[text()="Зарегистрироваться"]'  # Кнопка завершения регистрации после ввода данных
    button_enter_from_registr_of_fogot = By.XPATH, '//a[@href="/login"]'  # Кнопка перехода к форме логина, с форм регистрации и забыли пароль

