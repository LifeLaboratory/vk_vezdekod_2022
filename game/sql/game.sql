-- Table: public.game

-- DROP TABLE public.game;

CREATE TABLE IF NOT EXISTS public.game
(
  id_game integer NOT NULL,
  id_user integer NOT NULL,
  id_question integer NOT NULL DEFAULT 0,
  time_open timestamp without time zone DEFAULT now(),
  time_close timestamp without time zone,
  round integer DEFAULT 1,
  health double precision DEFAULT 10,
  food double precision DEFAULT 10,
  money double precision DEFAULT 10,
  communication double precision DEFAULT 10,
  point integer DEFAULT 0,
  value integer DEFAULT 5,
  id_person integer,
  status boolean,
  worked integer DEFAULT 0,
  call integer DEFAULT 0,
  CONSTRAINT game_pk PRIMARY KEY (id_game)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.game
  OWNER TO postgres;

-- Index: public.game_id_game_uindex

-- DROP INDEX public.game_id_game_uindex;

CREATE UNIQUE INDEX IF NOT EXISTS game_id_game_uindex
  ON public.game
  USING btree
  (id_game);

