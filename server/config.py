import os, secrets

from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'lux'
    
    
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
    
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.environ.get('MYSQL_DATABASE'))
    
    
settings = dict(local=DevelopmentConfig, prod=ProductionConfig, testing=TestingConfig)