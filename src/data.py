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

def check_email(enter_email):
    email = enter_email
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, email) is not None:
        print("Проверка пройдена")
        return True
    else:
        print("Провера не пройдена")
        return False

def wrong_email_cases():
    word = "word"
    word_and_dog = "word@"
    word_and_part_of_domen = "word@word"
    word_and_part_of_domen_with_point = "word@word."
    domen_without_dot = "@word"
    domen_with_dot = "@word.word"
    return (word, word_and_dog, word_and_part_of_domen, word_and_part_of_domen_with_point, domen_with_dot, domen_without_dot)

