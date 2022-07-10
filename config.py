from secrets import token_urlsafe

# Basic Config
class Config(object):
    DEBUG = False
    TESTING = False
    HOST = '127.0.0.1'

    SECRET_KEY = token_urlsafe(16)

    # Database
    DB_NAME = "development_db"
    DB_USERNAME = "pgadmin"
    DB_PASSWORD = "buTo1452"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = True

# Basic Config + extra config for production
class ProductionConfig(Config):
    pass

# Basic Config + extra config for testing
class TestingConfig(Config):
    TESTING = True

    SECRET_KEY = token_urlsafe(16)

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = False


# Basic Config + extra config for development
class DevelopmentConfig(Config):
    DEBUG = True

    SECRET_KEY = token_urlsafe(16)

    UPLOADS = "/home/kachnic_1186205/App/app/static/img"
    SESSION_COOKIE_SECURE = False