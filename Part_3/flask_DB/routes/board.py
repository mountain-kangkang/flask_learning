# API List

# /board
# 전체 게시글 불러오기(GET)
# 게시글 작성하기(POST)

# /board/<int:board_id>
# 하나의 게시글 불러오기(GET)
# 특정 게시글 수정하기(PUT)
# 특정 게시글 삭제하기(DELETE)

from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        return "success"

    def post(self):
        pass