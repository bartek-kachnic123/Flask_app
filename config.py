from secrets import token_urlsafe

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = token_urlsafe(16)

    DB_NAME = "db_production"
    DB_USERNAME = "db_user"
    DB_PASSWORD = "db_password"

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

    SECRET_KEY = token_urlsafe(16)

    DB_NAME = "db_development"
    DB_USERNAME = "db_user"
    DB_PASSWORD = "db_password"

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = False



class DevelopmentConfig(Config):
    DEBUG = True

    SECRET_KEY = token_urlsafe(16)

    DB_NAME = "db_development"
    DB_USERNAME = "db_user"
    DB_PASSWORD = "db_password"

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = False