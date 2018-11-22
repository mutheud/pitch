import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or '1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:diana@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''
    # pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SECRET_KEY = os.environ.get("SECRET_KEY")

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}