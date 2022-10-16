from selenium.webdriver.common.by import By

button_private_cabinet = By.XPATH, '//nav/a[@href="/account"]' # Кнопка личный кабинет в хедере сайта
button_enter_to_account_on_main_page = By.XPATH, '//button[text()="Войти в аккаунт"]' # Кнопка войти в аккаунт на главной странице
button_registration_complite = By.XPATH, '//button[text()="Зарегистрироваться"]' # Кнопка завершения регистрации после ввода данных
button_complite_login = By.XPATH, '//button[text()="Войти"]' # Кнопка завершения входа после ввода данных
button_eye_for_password = By.XPATH, '//*[contains(@d, "M12 ")]' # Кнопка глаза скрыть/показать пароль
button_restration_on_login_page = By.XPATH, '//a[text()="Зарегистрироваться"]' # Кнопка перехода к форме регистрации с формы логина
button_forgot_password = By.XPATH, '//a[@href="/forgot-password"]' # Кнопка перехода к форме забыли пароль с формы логина
button_enter_from_registr_of_fogot = By.XPATH, '//a[@href="/login"]' # Кнопка перехода к форме логина, с форм регистрации и забыли пароль
button_open_private_cabinet = By.XPATH, '//p[text()="Личный Кабинет"]' # Кнопка личный кабинет после логина
button_open_constructor = By.XPATH, '//p[text()="Конструктор"]' # Кнопка конструктора в хедере сайта
button_logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' # Кнопка лого в хедере сайта
button_exit_from_account = By.XPATH, '//button[text()="Выход"]' # Кнопка выход в личном кабинете
button_change_constructor_part_to_bread = By.XPATH, '//span[text()="Булки"]' # Кнопка перехода к разделу булки в конструкторе
button_change_constructor_part_to_sauce = By.XPATH, '//span[text()="Соусы"]' # Кнопка перехода к разделу соусы в конструкторе
button_change_constructor_part_to_fillings = By.XPATH, '//span[text()="Начинки"]' # Кнопка перехода к разделу начинки в конструкторе

input_email_for_login = By.XPATH, '//input[@name="name"]' # Ввод email при логине
input_password = By.XPATH, '//input[@name="Пароль"]' # Ввод пароля при логине
input_name_for_registration = By.XPATH, '//fieldset[1]/div/div/input' # Ввод имени при регистрации
input_email_for_registration = By.XPATH, '//fieldset[2]/div/div/input' # Ввод email при регистрации

error_wrong_password = By.XPATH, '//p[text()="Некорректный пароль"]' # Ошибки принеправильном пароле при регистрации
error_wrong_user_email = By.XPATH, '//p[text()="Такой пользователь уже существует"]' # Ошибка при регистрации пользователя

text_fillings = By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]' # Контрольное название начинки 6 тест
text_sause = By.XPATH, '//p[text()="Соус Spicy-X"]' # Контрольное название соуса 6 тест
text_bread = By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]' # Контрольное название хлеба 6 тест

