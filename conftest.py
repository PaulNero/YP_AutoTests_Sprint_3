import pytest
import random
import string
from src import links
from selenium import webdriver
import tempfile
import shutil

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
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
    driver.get(links.main_link)
    
    yield driver
    
    driver.quit()
    
    # Удаляем временную директорию
    try:
        shutil.rmtree(user_data_dir)
    except:
        pass

@pytest.fixture
def new_email():
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
    value = random.randint(1, 99999999)
    email = f'{title}{value}@test.test'
    return email
