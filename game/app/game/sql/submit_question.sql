select
  (q.answer::json -> {answer}::text ->> 'health')::int health,
  (q.answer::json -> {answer}::text ->> 'point')::int point,
  (q.answer::json -> {answer}::text ->> 'money')::int money,
  e.round event_round,
  g.round cur_round,
  g.id_game,
  e.id_event,
  g.id_question,
  g.id_user,
  q.good_answer,
  ((q.answer::json -> q.good_answer::text) ->> 'description')::text description
from
  game g

join question q on q.id_question = g.id_question
left join event e on e.id_event = (q.answer::json -> 0::text ->> 'id_event')::int
/*left join lateral (
      select
  ((q.answer::json -> q.good_answer::text) ->> 'description')::int description
      ) lt on true*/
where
  id_user = {id_user}
and status is true