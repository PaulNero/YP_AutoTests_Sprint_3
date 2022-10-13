import re

name = 'Paul'
password_right = 1234567890
password_6_symbols = 123456
password_wrong = 12345
delay = 10

email_for_login = "pavel_nerobov_qa_03@yandex.test"

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

