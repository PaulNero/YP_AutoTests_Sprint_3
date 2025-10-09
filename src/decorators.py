import allure
from src.utils import attach_screenshot_and_log



def with_error_handling(func):
    """Обёртка для технических функций (без лишних шагов)."""
    def wrapper(*args, **kwargs):
        driver = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            attach_screenshot_and_log(driver, name_prefix='FAIL', api_response=str(e))
            allure.attach(str(e), name=f"Ошибка в {func.__name__}", attachment_type=allure.attachment_type.TEXT)
            raise
    return wrapper


# Засоряет отчет техническими шагами :(
# def with_allure_step(step_description=None):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             driver = args[0]
#             step_name = step_description or f"Выполнение: {func.__name__}"
#             try:
#                 with allure.step(step_name):
#                     return func(*args, **kwargs)
#             except Exception as e:
#                 attach_screenshot_and_log(driver, name_prefix='FAIL', api_response=str(e))
#                 with allure.step(f'Ошибка в {func.__name__}: {str(e)}'):
#                     raise
#         return wrapper
#     return decorator