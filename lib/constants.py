import os
from lib.set_credentials import set_credentials

set_credentials() # this function sets secret informations. You have to write your own one

CREDENTIAL_ERROR=False
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")
CC_EMAIL = os.getenv("CC_MAIL") # optional
if not SENDER_EMAIL or not SENDER_PASSWORD:
    CREDENTIAL_ERROR=True