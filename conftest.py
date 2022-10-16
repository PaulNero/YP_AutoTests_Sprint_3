import pytest
import random
import string
from src import links
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(links.main_link)
    yield driver
    driver.quit()

@pytest.fixture
def new_email():
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
    value = random.randint(1, 99999999)
    email = f'{title}{value}@test.test'
    return email
