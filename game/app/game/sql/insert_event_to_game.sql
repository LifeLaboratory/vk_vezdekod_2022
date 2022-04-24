insert into event_to_game
(
id_event,
id_game,
round
)
values
(
{id_event},
{id_game},
{round}
)
returning
  id_game