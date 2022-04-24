from game.provider import Provider
from game.game import Game

__author__ = 'Чусовитин А.Р.'

class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_game_info(self, id_user):
        description = self.check_events(id_user)
        game = self.provider.get_game_info(id_user)
        if game:
            event_img = ''
            if isinstance(game.get('event'), dict) and game.get('event'):
                self.provider.delete_event_to_game(game.get('event').get('id_event_to_game'))
                game.get('event').pop('id_event_to_game')

            game['description'] = f'''{description} {game['description']}'''
            self.check_end_game(game, id_user)
            return game
        else:
            return {'error': 'Такой игры нет'}

    def check_end_game(self, game, id_user):
        game['end_game'] = False
        if game.get('money') <= 0 or game.get('health') <= 0 or game.get('next_quest'):
            self.provider.end_game(id_user)
            game['end_game'] = True

    def check_events(self, id_user):
        event = self.provider.get_event_status(id_user)
        description = ''
        if event:
            self.provider.update_game_if_event(event[0])
            self.provider.delete_event_to_game(event[0].get('id_event_to_game'))
            # description = f'''<br><br>Случилось событие: {event[0].get('description')}'''
            description = f'''Из-за ваших предыдущих действий  {event[0].get('description')}<br><br>'''
        return description

    def send_game_answer(self, data):
        good_description = Game().submit_question(data)
        game_info = self.get_game_info(data.get('id_user'))
        if good_description:
            game_info['good_description'] = f'Стоит поступить иначе: {good_description}'
        else:
            game_info['good_description'] = 'Хороший выбор!'
        return game_info

    def get_game_events(self, id_user):
        return self.provider.get_game_events(id_user)

    def execute_game_action(self, data):
        return self.provider.execute_game_action(data)

    def start_new_game(self, data):
        self.provider.end_game(data.get('id_user'))
        Game().start_game(data)
        return self.get_game_info(data.get('id_user'))
