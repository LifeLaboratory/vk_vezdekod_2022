"""Рeализация игры"""

from base.provider import Provider

__author__ = 'Чусовитин А.Р.'


class Game:

    def __init__(self):
        self.db = Provider('./game/sql')

    def start_game(self, params):
        self.db.exec_by_file('start_game.sql', params)

    def submit_question(self, params):
        submit = self.db.exec_by_file('submit_question.sql', params)[0]
        good_answer = None
        if int(submit.get('good_answer')) != int(params.get('answer')[1]):
            good_answer = submit.get('description')
        params = {
            'id_event': submit.get('id_event'),
            'id_question': submit.get('id_question'),
            'id_game': submit.get('id_game'),
            'id_user': submit.get('id_user'),
            'health': submit.get('health') or 0,
            'point': submit.get('point') or 0,
            'money': submit.get('money') or 0,
            'answer': params.get('answer'),
        }
        self.db.exec_by_file('insert_history_question.sql', params)
        if submit.get('id_event'):
            params = {
                'id_event': submit.get('id_event'),
                'id_game': submit.get('id_game'),
                'round': submit.get('event_round') + submit.get('cur_round'),
            }
            self.db.exec_by_file('insert_event_to_game.sql', params)
        params = {
            'id_question': submit.get('id_question'),
            'id_game': submit.get('id_game'),
            'health': submit.get('health') or 0,
            'point': submit.get('point') or 0,
            'money': submit.get('money') or 0,
        }
        self.db.exec_by_file('next_game.sql', params)
        return good_answer

