import os

from dotenv import load_dotenv

from integration import KavenegarSMSService

# Load Environment Variables from .env file
load_dotenv()

KAVENEGAR_API_KEY = os.getenv('KAVENEGAR_API_KEY', '')
KAVENEGAR_MAIN_URL = os.getenv('KAVENEGAR_MAIN_URL', 'https://api.kavenegar.com')
KAVENEGAR_API_VERSION = os.getenv('KAVENEGAR_API_VERSION', 'v1')
KAVENEGAR_SEND_SMS_ENDPOINT = os.getenv('KAVENEGAR_SEND_SMS_ENDPOINT', 'sms/send.json')

# Overwrite Message Text Based On Contact Phone Number Or Not
OVERWRITE_MESSAGE_TEXT = True

# SMS Service Instance
SMS_SERVICE = KavenegarSMSService()
