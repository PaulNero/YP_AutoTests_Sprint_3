from dotenv import load_dotenv
import os

load_dotenv()

main_link = os.getenv('MAIN_LINK')

login_link = 'login'
register_link = 'register'
forgot_password_link = 'forgot-password'
private_cabinet = 'account/profile'
