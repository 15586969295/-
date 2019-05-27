from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging
from logging.handlers import RotatingFileHandler


# 初始化数据库
db = SQLAlchemy()


def setup_log():
    # 设置日志的记录等级
    logging.basicConfig(level=Config.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app():
    app = Flask(__name__, template_folder="../front_end/templates", static_folder='../front_end/static')
    # 加载配置
    app.config.from_object(Config)
    # 通过app初始化
    db.init_app(app)
    # 注册蓝图
    from back_end.modules.index import index_blu
    from back_end.modules.game import game_blu
    from back_end.modules.leaderboard import leaderboard_blu
    app.register_blueprint(index_blu)
    app.register_blueprint(game_blu)
    app.register_blueprint(leaderboard_blu)
    return app
