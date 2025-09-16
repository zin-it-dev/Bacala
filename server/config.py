import os, secrets

from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'lux'
    CSRF_ENABLED = True
    EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = os.environ.get('REDIS_URL')
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    
    url_object = URL.create(
        "mysql+pymysql",
        username=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        host=os.environ.get('MYSQL_HOST'),
        port=os.environ.get('MYSQL_PORT'),
        database=os.environ.get('MYSQL_DATABASE')
    )
    SQLALCHEMY_DATABASE_URI = url_object
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    MAIL_SUPPRESS_SEND = False
    SQLALCHEMY_RECORD_QUERIES = True
    
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.environ.get('MYSQL_DATABASE'))
    CACHE_TYPE = 'SimpleCache'
    
    
settings = dict(local=DevelopmentConfig, prod=ProductionConfig, testing=TestingConfig)