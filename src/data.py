import re
from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv('NAME')
password_right = os.getenv('PASSWORD_RIGHT')
password_6_symbols = os.getenv('PASSWORD_6_SYMBOLS')
password_wrong = os.getenv('PASSWORD_WRONG')
delay = os.getenv('DELAY')

email_for_login = os.getenv('EMAIL_FOR_LOGIN')

error_user_text = "Такой пользователь уже существует"
error_password_text = "Некорректный пароль"
