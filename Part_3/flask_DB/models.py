# Model -> Table 생성
# 게시글 -> board
# 유저 -> user

from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards')


# 원래는 이렇게 하나의 python 파일이 이니라 
# models 폴더에서 테이블마다 따로 python 파일을 만들어서 관리하는듯 하다
# models/users.py, models/board.py 이런식으로 말이다.