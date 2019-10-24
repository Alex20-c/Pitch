import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'd8dcaac6a9ab4f86a4a9fbd07fa4372b'

    DEBUG = True


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'
    pass


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:aleki@localhost/pitches'


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
