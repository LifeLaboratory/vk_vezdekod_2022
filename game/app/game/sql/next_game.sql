with
solved_question as (
select
distinct id_question
from question_history
where id_game = {id_game}
),
count_question as (
  select
    count(1) as count_quest
  from question
),
count_solve_question as (
  select
    count(1) as count_solve_quest
  from solved_question
),
uniq_quest as (
  (
    select id_question, True as next_quest
    from question, count_question, count_solve_question
    where
      id_question != {id_question}::int
      and id_question not in (table solved_question)
      and count_quest > count_solve_quest
    order by random () limit 1
  )
  union
  (
  select id_question, False as next_quest
  from question, count_question, count_solve_question
  where
    id_question != {id_question}::int
    and count_quest <= count_solve_quest
  order by random () limit 1
  )
    )
update game
set
    id_question = (
        select id_question
        from uniq_quest
        ),
    round = round + 1,
    point = coalesce(point, 0) + coalesce({point}, 0),
    health = health + coalesce({health}, 0),
    money = money + coalesce({money}, 0)
WHERE
id_game = {id_game}