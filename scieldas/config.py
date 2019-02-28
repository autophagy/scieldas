import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    GITHUB_API_KEY = os.environ.get("GITHUB_API_KEY")
    TRAVIS_API_KEY = os.environ.get("TRAVIS_API_KEY")
    REQUEST_CACHE_SECONDS = os.environ.get("REQUESTS_CACHE_SECONDS", 300)
    IMAGE_CACHE_COUNT = os.environ.get("IMAGE_CACHE_COUNT", 5000)
    COMMIT_SHA = os.environ.get("COMMIT_SHA")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.environ.get("GITHUB_CLIENT_SECRET")
    TOKEN_DB_REFRESH_SECONDS = 3600

    logging.basicConfig(
        format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S %z",
    )


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir + "/test.db"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
