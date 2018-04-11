import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    REDIS_URL = os.environ.get("REDIS_URL")


class DevelopmentConfiguration(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'issues.sqlite')
    REDIS_URL = "redis://localhost:6379"


class TestingConfiguration(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'issues.sqlite')
    PAGE_LIMIT = 2
    REDIS_URL = "redis://localhost:6379"


config = {
    'production': Config,
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration
}
