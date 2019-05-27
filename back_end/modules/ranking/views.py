from . import ranking_blu
from back_end.models import Player,Season,tb_player_season
from flask import current_app
import json


@ranking_blu.route('/games')
def rankings():
    rankings_list = []
    try:
        games_list = Game.query.order_by(Game.create_time.desc())

    except Exception as e:
        current_app.logger.error(e)

    rankings_dict_li = []
    for game in games_list:
        game_dict_li.append(game.to_dict())

    data = {
        'game_dict_li': game_dict_li
    }
    print(data)

    return json.dumps(data)
