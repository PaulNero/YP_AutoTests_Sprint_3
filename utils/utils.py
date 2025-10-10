import allure
import re
import json
from datetime import datetime
from allure_commons.types import AttachmentType

def attach_screenshot_and_log(driver, name_prefix='Error', api_response=None):
    try:
        screenshot = driver.get_screenshot_as_base64()
        allure.attach(screenshot, 
                    name=f'{name_prefix} {datetime.now().strftime("%Y-%m-%d %H-%M-%S")}',
                    attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        allure.attach(
            f'Не удалось сделать скриншот: {e}',
            name='Screenshot Error',
            attachment_type=AttachmentType.TEXT
        )
    if api_response:
        try:
            parsed = json.loads(api_response) if isinstance(api_response, str) else api_response
            allure.attach(
                json.dumps(parsed, ensure_ascii=False, indent=2),
                name='API response',
                attachment_type=allure.attachment_type.JSON
            )
        except Exception:        
            allure.attach(
                str(api_response),
                name='API/EXception data',
                attachment_type=AttachmentType.TEXT
            )
            
def check_email(enter_email):
    email = enter_email
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, email) is not None:
        print("Проверка пройдена")
        return True
    else:
        print("Провера не пройдена")
        return False
