from secrets import token_urlsafe

class Config(object):
    DEBUG = False
    TESTING = False
    HOST = '127.0.0.1'

    SECRET_KEY = token_urlsafe(16)

    # Database
    DB_NAME = "db_production"
    DB_USERNAME = "db_user"
    DB_PASSWORD = "db_password"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{HOST}/{DB_NAME}'

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

    SECRET_KEY = token_urlsafe(16)

    # Database
    DB_NAME = "db_development"
    DB_USERNAME = "pgadmin"
    DB_PASSWORD = "buTo1452"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{Config.HOST}/{DB_NAME}'

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = False



class DevelopmentConfig(Config):
    DEBUG = True

    SECRET_KEY = token_urlsafe(16)

    # Database
    DB_NAME = "db_development"
    DB_USERNAME = "pgadmin"
    DB_PASSWORD = "buTo1452"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{Config.HOST}/{DB_NAME}'

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = False