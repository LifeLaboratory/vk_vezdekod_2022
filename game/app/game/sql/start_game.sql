INSERT INTO game
    (
     id_user,
     id_question,
     time_open,
     round,
     health,
     point,
     money,
     id_person,
     status
     )
select
 {id_user},
 (select id_question from question order by random () limit 1),
 now(),
 1,
 person.health,
 person.point,
 person.money,
 person.id_person,
 true
FROM
  person
WHERE
  person.id_person = {id_person}
