import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DISK_SPACE_TOP_N = 10
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    @classmethod
    def init_app(cls, app):
        pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}