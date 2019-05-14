from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# 初始化数据库
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(Config)
    # 通过app初始化
    db.init_app(app)
    return app

