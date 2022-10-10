import re
import pytest


@pytest.fixture
def check_email(enter_email):
    email = enter_email
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, email) is not None:
        print("Проверка пройдена")
        return True
    else:
        print("Провера не пройдена")
        return False


