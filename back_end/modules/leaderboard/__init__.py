from flask import Blueprint

# 创建蓝图对象
leaderboard_blu = Blueprint("leaderboard", __name__)

from . import views
