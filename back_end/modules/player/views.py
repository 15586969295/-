from . import player_blu
from back_end.models import Player
from flask import current_app
import json


@player_blu.route('/player')
def players():
    players_list = []
    try:
        players_list = Player.query.order_by(Player.season.desc())
    except Exception as e:
        current_app.logger.error(e)

    player_dict_li = []
    for player in players_list:
        player_dict_li.append(player.to_dict())

    data = {
        'player_dict_li': player_dict_li
    }
    print(data)

    return json.dumps(data)
