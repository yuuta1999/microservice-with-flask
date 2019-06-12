# users/app/config.py

import os

class BaseConfig(object):
    """Base configuration variables used in all environments. 
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TESTING = False
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ACCESS_TOKEN_EXPIRE = 30

class DevConfig(BaseConfig):
    """Environment variables used in development mode.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(BaseConfig):
    """Environment variables used in testing mode.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
    TESTING = True
    ACCESS_TOKEN_EXPIRE = 1
