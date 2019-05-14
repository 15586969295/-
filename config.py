import logging


class Config(object):
    """项目的配置"""
    DEBUG = True

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_rento"  # mysql://username:password@ip:port/dbname
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LELVEL = logging.DEBUG