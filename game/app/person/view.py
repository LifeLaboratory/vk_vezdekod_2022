from flask import jsonify
from base import app
from person.processor import Processor
from base.helper import make_response

__author__ = 'Чусовитин А.Р.'


PREFIX = '/api/person'


@app.route(PREFIX, methods=['GET', 'OPTIONS'])
def all_person():
    func = {
        'id_person': 1,
        'name': 'Студент',
        'description': 'Все мы немного студенты и хотим кушать',
        'pic': 'https://emojio.ru/images/apple-b/1f468-200d-1f393.png',
        'health': 10.0,  # Здоровье
        'food': 5.0,  # Питание
        'leisure': 3.0,  # Досуг
        'communication': 4.0,  # Общение
        'value': 3,  # количество денег
    }
    return make_response(jsonify(Processor().all_person()))
