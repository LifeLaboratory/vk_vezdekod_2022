from flask import request, jsonify
from base import app
from rating.processor import Processor
from base.helper import session_to_id_user
from base.helper import make_response

__author__ = 'Чусовитин А.Р.'


PREFIX = '/api/rating'


@app.route(PREFIX, methods=['GET', 'OPTIONS'])
def all_rating():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    id_user = session_to_id_user(request.headers) or None
    top = Processor().get_top_users(id_user)
    func = {
        'top': top
    }
    answer = jsonify(func)
    return make_response(answer)
