import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATA_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL.PASSWORD')

   
    @staticmethod

    def init_app(app):

        pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql+psycopg2://alex:aleki@localhost/pitches')
    # pass


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'
    
    DEBUG = True

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
