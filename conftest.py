import pytest
import random
import string
import allure
from src import links
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import tempfile
import shutil
from datetime import datetime


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox') # Необходимо для запуска Chrome в Docker/CI окружении
    options.add_argument('--disable-dev-shm-usage') # Необходимо для запуска Chrome в Docker/CI окружении
    
    # Создаём уникальную временную директорию для каждого теста
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    
    driver = webdriver.Chrome(options=options)
    test_name = request.node.name
    print(f"\n[DRIVER STARTED] {test_name}")

    try:
        with allure.step(f'Открыть главную страницу: {links.main_link}'):
            driver.get(links.main_link)
    except WebDriverException as e:
        error_message = f'Сервис {links.main_link} недоступен - тест "{test_name}" пропущен.\nОшибка: {str(e)}'
        print(f"[ERROR] {error_message}")
        with allure.step("Ошибка подключения к сайту"):
            allure.attach(str(e), name="Дополнительная информация", attachment_type=allure.attachment_type.TEXT)
        pytest.skip(error_message)
    else:
        yield driver
    finally:
        with allure.step('Закрытие драйвера и очистка ресурсов'):
            try:
                driver.quit()
                print(f"[DRIVER CLOSED] {test_name}")
            except Exception as e:
                print(f"[ERROR] Ошибка при закрытии драйвера: {e}")
            # Удаляем временную директорию
            shutil.rmtree(user_data_dir)



@pytest.fixture
def new_email():
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
    value = random.randint(1, 99999999)
    email = f'{title}{value}@test.test'
    return email
