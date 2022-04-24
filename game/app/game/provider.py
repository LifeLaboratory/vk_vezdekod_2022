import base.provider as bp

__author__ = 'Чусовитин А.Р.'


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'session'
        self.field = ['is_user', 'id_session']

    def get_game_info(self, id_user):
        self.query = f'''

SELECT
  g.id_question::int4 id_question
, q.description::text description
, q.pic::text pic
, q.answer::json answer
, g.round::int4 round
, g.health::int4 health
, g.money::int4 money
, g.point::int4 point
, p.pic::text as person_pic
, CASE WHEN e.id_event is not null THEN
  json_build_object('id_event', e.id_event, 'description', e.description, 'money', -1, 'health', -1, 'point', -1, 'id_event_to_game', etg.id_event_to_game)::json
ELSE
  json_build_object()::json
END as event
, case when g.health <= 0 or g.money <= 0 then True else False end as end_game

FROM game g
left join person p using(id_person)
LEFT JOIN question q ON q.id_question = g.id_question
LEFT JOIN event_to_game etg ON (etg.id_game = g.id_game and etg.round <= g.round)
LEFT JOIN event e on etg.id_event = e.id_event
WHERE g.status = True and g.id_user = {id_user}
ORDER BY etg.id_event_to_game ASC
LIMIT 1
'''
        answer = self.execute()[0]
        for answ in range(len(answer.get('answer')) -1):
            answer.get('answer')[str(answ)].pop('health')
            answer.get('answer')[str(answ)].pop('point')
            answer.get('answer')[str(answ)].pop('money')
        return answer

    def delete_event_to_game(self, id_event_to_game):
        self.query = f'''
DELETE FROM event_to_game WHERE id_event_to_game = {id_event_to_game} RETURNING id_event
'''
        return self.execute()[0]

    def send_game_answer(self, answer):
        self.query = f''''''
        return self.execute()[0]

    def get_game_events(self, answer):
        self.query = f''''''
        return self.execute()

    def execute_game_action(self, id_user):
        self.query = f''''''
        return self.execute()[0]

    def check_session(self, session):
        self.query = f''''''
        return self.execute()[0]

    def get_event_status(self, id_user):
        self.query = f'''
with get_game as (
  select id_game
   , round
  FROM game g
  WHERE g.status = True and g.id_user = {id_user}
  LIMIT 1
),
active_event as (
  select event.*
    , id_game
    , etg.id_event_to_game
  from event_to_game etg
  left join event using (id_event)
  where etg.id_game = any(array(select id_game from get_game limit 1))
    and etg.round <= (select round from get_game limit 1)
    -- and event.tags && (select tags from question where id_question = (select id_question from get_game))
  limit 1
)
table active_event
        '''
        return self.execute()

    def update_game_if_event(self, event):
        self.query = f'''
update game
set 
  health = coalesce(health, 0) + coalesce({event.get('health')}::int, 0)
  , money = coalesce(money, 0) + coalesce({event.get('money')}::int, 0)
  , point = 
    case when coalesce(point, 0) + coalesce({event.get('point')}::int, 0) >= 0
      then coalesce(point, 0) + coalesce({event.get('point')}::int, 0)
    else 0
    end
where id_game = {event.get('id_game')}::int
'''
        self.execute()

    def end_game(self, id_user):
        """
        Метод для завершения всех игр пользователя
        :param id_user:
        :return:
        """
        self.query = f'''
update game
set status = false
where id_user = {id_user}
  and status is true
        '''
        return self.execute()
