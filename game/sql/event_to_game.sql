-- Table: public.event_to_game

-- DROP TABLE public.event_to_game;
CREATE SEQUENCE IF NOT EXISTS event_to_game_id_event_seq START 1;

CREATE TABLE IF NOT EXISTS public.event_to_game
(

  id_event_to_game integer NOT NULL DEFAULT nextval('event_to_game_id_event_seq'::regclass),
  id_event integer,
  id_game integer,
  round integer,
  CONSTRAINT id_event_to_game_pk PRIMARY KEY (id_event_to_game)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.event_to_game
  OWNER TO postgres;

