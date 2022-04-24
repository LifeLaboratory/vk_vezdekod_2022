from flask import request, jsonify
from base import app
from users.processor import Processor
from base.helper import session_to_id_user
from base.helper import make_response

__author__ = 'Чусовитин А.Р.'


PREFIX = '/api/user'


@app.route(PREFIX, methods=['GET'])
def all_user():
    return make_response(jsonify(Processor().users()))


@app.route(PREFIX + '/profile', methods=['GET', 'OPTIONS'])
def profile_user():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    id_user = session_to_id_user(request.headers)
    answer = Processor().profile(id_user)
    if answer:
        answer = answer[0]
    else:
        answer = {}
    return make_response(jsonify(answer))


@app.route(PREFIX + '/<int:id_user>', methods=['GET', 'OPTIONS'])
def profile(id_user):
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    answer = Processor().profile(id_user)
    if answer:
        answer = answer[0]
    else:
        answer = {}
    return make_response(jsonify(answer))


@app.route(PREFIX + '/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    data = request.json
    res = Processor().login(data)
    return make_response(jsonify(res))


@app.route(PREFIX + '/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    data = request.json
    res = Processor().create(data)
    return make_response(jsonify(res))
