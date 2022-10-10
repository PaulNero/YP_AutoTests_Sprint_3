# Финальное задание:  Sprint_3

## Корень проекта:
### conftest.py:   
> Содержит фикстуру для проверки формата email.

### Папка scr:
#### data.py
> Содержит статичные данные используемые в тестах.

#### driver_settings.py
> Содержит настройки для браузеров, пока минимальные, просто инициализация драйвера.   
> Тесты написаны для трёх браузеров: chrome, firefox и safari.   
> В названии каждого теста, есть название браузера в котором он запустится.

#### links.py
> Содержит базовый url для тестов и ручки на которые нужно ориентироваться при переходе по страницам.

#### locators.py
> Содержит локаторы на которые ориентируется драйвер при прохождении тестов.

### tests:
> test_all_browsers()

В каждом тесте содержится функция для запуска всех тестов во всех браузерах. 
#### test_01_registration.py
Содержит позитивные и негативные тесты для регистрации:  

Positive:  
> test_registration_via_private_cabinet_chrome_success()

Регистрация при переходе через личный кабинет.   
> test_registration_via_chrome_enter_to_account_browser_success()

Регистрация при переходе через кнопку "Войти в аккаунт".  

Negative:   
> test_field_name_not_empty_chrome_failed_registration()

Проверка, что поле имя при регистрации не может быть пустым.  
> test_wrong_password_error_chrome_failed_registration()

Проверка появления ошибки при вводе неверного пароля.  
> test_minimal_len_password_chrome_failed_registration()

Проверка минимальной длины пароля в 5 символов.  
> test_email_format_chrome_failed_registration()

Проверка формата email при регистрации.

#### test_02_login.py
> test_login_page_via_private_cabinet_button_chrome_success()

Проверка логина через личный кабинет.  
> test_login_page_via_enter_account_button_chrome_success() 

Проверка логина через кнопку "Войти в аккаунт"   
> test_login_page_via_registration_chrome_success()

Проверка логина после возврата на страницу логина со страницы регистрации.  
> test_login_page_via_forgot_password_chrome_success() 

Проверка логина после возврата на страницу логина со страницы "Забыли пароль". 

#### test_03_enter_to_private_cabinet.py
> test_enter_private_cabinet_chrome_success() 

Проверка перехода в личный кабинет после логина

#### test_04_open_constructor_via_cabinet.py
> test_enter_constructor_from_cabinet_via_constructor_button_chrome_success()
 
Проверка перехода к конструктору через личный кабинет.

#### test_05_exit_from_account.py
> test_exit_private_cabinet_chrome_success()
 
Проверка выхода из аккаунта.

#### test_06_change_constructor_parts.py
> test_change_constructor_parts_chrome_parts_changed()

Проверка переключения разделов конструктора.