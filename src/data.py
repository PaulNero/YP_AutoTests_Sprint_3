import random
import string

name = 'Paul'
password_right = 1234567890
password_6_symbols = 123456
password_wrong = 12345
delay = 10

email_for_login = "pavel_nerobov_qa_03@yandex.test"

error_user_text = "Такой пользователь уже существует"
error_password_text = "Некорректный пароль"

def wrong_email_cases():
    word = "word"
    word_and_dog = "word@"
    word_and_part_of_domen = "word@word"
    word_and_part_of_domen_with_point = "word@word."
    domen_without_dot = "@word"
    domen_with_dot = "@word.word"
    return (word, word_and_dog, word_and_part_of_domen, word_and_part_of_domen_with_point, domen_with_dot, domen_without_dot)

def new_email():
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
    value = random.randint(1, 99999999)

    email = f'{title}{value}@test.test'

    return email