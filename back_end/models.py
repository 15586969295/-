from datetime import datetime
from . import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


tb_player_season = db.Table('tb_player_season',
                            db.Column('player_id', db.Integer, db.ForeignKey('tb_player.id'), primary_key=True),
                            db.Column('season_id', db.Integer, db.ForeignKey('tb_season.id'), primary_key=True),
                            )


class Player(BaseModel, db.Model):
    """选手"""
    __tablename__ = "tb_player"

    id = db.Column(db.Integer, primary_key=True)  # 选手编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 选手昵称
    season = db.relationship('Season', secondary=tb_player_season, backref='player', lazy='dynamic')

    def to_dict(self):
        resp_dict = {
            'id': self.id,
            'nick_name': self.nick_name,
            'season_detials': self.season.all()
        }

        return resp_dict


class Season(BaseModel, db.Model):
    """赛季"""
    __tablename__ = "tb_season"

    id = db.Column(db.Integer, primary_key=True)  # 赛季编号
    score = db.Column(db.Integer, nullable=False)  # 得分
    win = db.Column(db.Integer, nullable=False)  # 胜场
    total = db.Column(db.Integer, nullable=False)  # 当前总场次
    players = db.relationship('Player', secondary=tb_player_season, backref='season', lazy='dynamic')
    games = db.relationship('Game', lazy='dynamic')  # 当前赛季的所有对局

    def to_dict(self):
        resp_dict = {
            'id': self.id,
            'games': self.games.all()
        }

        return resp_dict


class Game(BaseModel, db.Model):
    """对局"""
    __tablename__ = "tb_game"

    season_id = db.Column(db.Integer, db.ForeignKey("tb_season.id"))  # 赛季id
    id = db.Column(db.Integer, primary_key=True)  # 对局编号
    first = db.Column(db.String(20), nullable=False)  # 第一名选手
    second = db.Column(db.String(20), nullable=False)  # 第二名选手
    third = db.Column(db.String(20), nullable=False)  # 第三名选手
    fourth = db.Column(db.String(20), nullable=False)  # 第四名选手
    fifth = db.Column(db.String(20), nullable=False)  # 第五名选手
    sixth = db.Column(db.String(20), nullable=False)  # 第六名选手

    def to_dict(self):
        resp_dict = {
            'id': self.id,
            'season_id': self.season_id,
            'first': self.first,
            'second': self.second,
            'third': self.third,
            'fourth': self.fourth,
            'fifth': self.fifth,
            'sixth': self.sixth,
            'time': self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }

        return resp_dict
