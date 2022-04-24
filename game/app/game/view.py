from flask import request, jsonify
from base import app
from game.processor import Processor
from base.helper import session_to_id_user, check_session
from base.helper import make_response

__author__ = 'Чусовитин А.Р.'


PREFIX = '/api/game'


@app.route(PREFIX, methods=['GET', 'POST', 'OPTIONS'])
def get_game_info():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    if request.method == 'GET':
        id_user = session_to_id_user(request.headers)
        return make_response(jsonify(Processor().get_game_info(id_user)))
    if request.method == 'POST':
        data = request.json
        check_session(data, request.headers)
        return make_response(jsonify(Processor().start_new_game(data)))


@app.route(PREFIX + '/question', methods=['POST', 'OPTIONS'])
def send_game_answer():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))

    json_data = request.json
    id_user = session_to_id_user(request.headers)
    json_data['id_user'] = id_user
    return make_response(jsonify(Processor().send_game_answer(json_data)))
