from flask import Blueprint

# 创建蓝图对象
game_blu = Blueprint("game", __name__)

from . import views
