import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'edu_crm_secret_key_2024')
    DEBUG = True