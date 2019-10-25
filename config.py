import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATA_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
            
    # emails configuration
    
    MAIL_SERVER=os.environ.get('MAIL_SERVER')

    MAIL_PORT=os.environ.get('MAIL_PORT')

    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')

    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')

    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

    DEBUG = True      
  
    
    @staticmethod

    def init_app(app):

        pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    
class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'
    
  


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
