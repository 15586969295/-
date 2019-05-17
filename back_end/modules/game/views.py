from . import game_blu
from back_end.models import Game
from flask import current_app
import json


@game_blu.route('/games')
def games():
    games_list = []
    try:
        games_list = Game.query.order_by(Game.create_time.desc())
    except Exception as e:
        current_app.logger.error(e)

    game_dict_li = []
    for game in games_list:
        game_dict_li.append(game.to_dict())

    data = {
        'game_dict_li': game_dict_li
    }
    print(data)

    return json.dumps(data)
