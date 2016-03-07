import os, sae
basedir = os.path.abspath(os.path.dirname(__file__))
from sae.const import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS,  MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'registerany@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Registeranything'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <registerany@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME=0.5

    @staticmethod
    def init_app(app):
        pass



class DevelopmentConfig(Config):
    DEBUG = True
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
 #       'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS,  MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

class TestingConfig(Config):
    TESTING = True
   # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
   #     'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS,  MYSQL_HOST, MYSQL_PORT, MYSQL_DB)



class ProductionConfig(Config):
 #   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
  #      'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS,  MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

    @classmethod
    def init_app(cls,app):
        Config.init_app(app)

        import logging
        from logging.hanlders import SMTPHandler
        credentials=None
        secure=None
        if getattr(cls, 'MAIL_USERNAME',None) is not None:
            credentials=(cls.MAIL_USERNAME,cls.MAIL_PASSWORD)
            if getattr(cls,'MAIL_USE_SSL',None):
                secure=()
        mail_handler=SMTPHander(
            mailhost=(cls.MAIL_SERVER,cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX+' Application Error',
            credential=credentials,
            secure=secure)
        mail_handler.setLevel(Logging.ERROR)
        app.logger.addHander(mail_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
