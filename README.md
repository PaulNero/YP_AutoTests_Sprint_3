# YP AutoTests Sprint 3

Автоматизированное тестирование веб-приложения Stellar Burgers с использованием Selenium WebDriver, pytest и Page Object Model.

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10+
- Poetry (для управления зависимостями)
- Chrome/Chromium браузер

### Установка зависимостей
```bash
poetry install
```

### Настройка переменных окружения
Создайте файл `.env` в корне проекта со следующими переменными:
```env
MAIN_LINK=https://stellarburgers.nomoreparties.site
NAME=Тестовый Пользователь
PASSWORD_RIGHT=password123
PASSWORD_6_SYMBOLS=123456
PASSWORD_WRONG=wrongpass
EMAIL_FOR_LOGIN=test@example.com
DELAY=5
```

## 🧪 Запуск тестов

### Локальный запуск
```bash
# Запуск всех тестов
poetry run pytest -v -s tests

# Запуск с генерацией Allure отчетов
Отчеты генерируются автоматически при каждом запуске, что бы изменить, нужно убрать "addopts = --alluredir=allure-results" в pytest.ini

Тогда для генериции запускать:
poetry run pytest --alluredir=allure-results
poetry run allure serve allure-results
```

### Запуск по маркерам
```bash
# Тесты регистрации
poetry run pytest -m registration

# Тесты логина
poetry run pytest -m login

# Тесты личного кабинета
poetry run pytest -m private_cabinet

# Тесты конструктора
poetry run pytest -m constructor

```

## 🏗️ Архитектура проекта

### Структура каталогов
```
├── pages/                    # Page Object Model
│   ├── base_page.py         # Базовый класс для всех страниц
│   ├── page_constructor/    # Страница конструктора бургеров
│   ├── page_forgot_password/# Страница восстановления пароля
│   ├── page_header/         # Шапка сайта
│   ├── page_login/          # Страница авторизации
│   ├── page_private_cabinet/# Личный кабинет
│   └── page_registration/   # Страница регистрации
├── src/                     # Исходные данные и конфигурация
│   ├── data.py             # Тестовые данные
│   └── links.py            # URL-адреса и маршруты
├── tests/                   # Тестовые сценарии
│   ├── test_01_registration.py
│   ├── test_02_login.py
│   ├── test_03_private_cabinet.py
│   └── test_04_constructor.py
├── utils/                   # Вспомогательные утилиты
│   ├── assertion.py        # Утилиты для проверок
│   ├── decorators.py       # Декораторы
│   ├── setup_method.py     # Базовые UI методы
│   ├── utils.py            # Общие утилиты
│   └── wait_er.py          # Ожидания и синхронизация
├── conftest.py             # Pytest конфигурация и фикстуры
├── pyproject.toml          # Poetry конфигурация
├── pytest.ini             # Pytest настройки
├── Dockerfile              # Docker образ для CI/CD
└── Jenkinsfile             # Jenkins pipeline
```

### Технологический стек
- **Python 3.10+** - основной язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **pytest** - фреймворк для тестирования
- **Allure** - генерация отчетов о тестировании
- **Poetry** - управление зависимостями
- **Page Object Model** - паттерн организации кода

## 📋 Покрытие тестами

### Регистрация (`test_01_registration.py`)
- ✅ Регистрация через личный кабинет
- ✅ Регистрация через кнопку "Войти в аккаунт"
- ❌ Валидация обязательного поля "Имя"
- ❌ Валидация формата пароля
- ❌ Валидация минимальной длины пароля (6 символов)
- ❌ Валидация формата email

### Авторизация (`test_02_login.py`)
- ✅ Логин через личный кабинет
- ✅ Логин через кнопку "Войти в аккаунт"
- ✅ Логин после возврата со страницы регистрации
- ✅ Логин после возврата со страницы восстановления пароля

### Личный кабинет (`test_03_private_cabinet.py`)
- ✅ Переход в личный кабинет после авторизации

### Конструктор (`test_04_constructor.py`)
- ✅ Переход к конструктору через личный кабинет
- ✅ Переключение разделов конструктора (булки, соусы, начинки)
- ✅ Выход из личного кабинета

## 🐳 CI/CD

### Jenkins Pipeline
Проект настроен для автоматического запуска в Jenkins:
- **Триггер**: Push в репозиторий GitHub
- **Docker образ**: `nerobovp/npn-test-chrome-python-allure:latest`
- **Отчеты**: Allure + JUnit XML
- **Параметры запуска**: выбор тестовых маркеров

### Docker
Готовый Docker образ включает:
- Python 3.10
- Chrome браузер
- Все необходимые зависимости
- Настройки для headless режима

## 🔧 Конфигурация

### Pytest маркеры
```ini
positive          # Позитивные тестовые сценарии
negative          # Негативные тестовые сценарии
registration      # Тесты регистрации
login             # Тесты авторизации
private_cabinet   # Тесты личного кабинета
constructor       # Тесты конструктора
```

### Особенности настройки
- **Headless режим**: тесты запускаются в фоновом режиме
- **Изоляция**: каждый тест использует отдельную временную директорию
- **Обработка ошибок**: автоматический пропуск тестов при недоступности сервиса
- **Очистка ресурсов**: автоматическое удаление временных файлов

## 📊 Отчеты

### Allure Reports
```bash
# Генерация отчета
poetry run allure serve allure-results

# Сборка статического отчета
poetry run allure generate allure-results --clean -o allure-report
```

### JUnit XML
Результаты тестов также экспортируются в формате JUnit XML для интеграции с CI/CD системами.


## 📝 Лицензия

Этот проект создан в рамках учебной программы Яндекс.Практикума.

## 👨‍💻 Автор

**PaulNero** - [58290662+PaulNero@users.noreply.github.com](mailto:58290662+PaulNero@users.noreply.github.com)

---

*Последнее обновление: $(date)*