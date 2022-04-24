-- Table: public.question_history

-- DROP TABLE public.question_history;

CREATE SEQUENCE IF NOT EXISTS question_history_id_question_history_seq START 1;

CREATE TABLE IF NOT EXISTS public.question_history
(
    id_question_history integer NOT NULL DEFAULT nextval('question_history_id_question_history_seq'::regclass),
    id_user integer NOT NULL,
    id_question integer NOT NULL,
    id_game integer NOT NULL,
    date_time_solve timestamp without time zone DEFAULT now(),
    answer integer NOT NULL,
    health double precision DEFAULT 10,
    point double precision DEFAULT 10,
    money double precision DEFAULT 10,
    CONSTRAINT id_question_history_pk PRIMARY KEY (id_question_history)
    )

WITH (
  OIDS=FALSE
  );

ALTER TABLE public.game
  OWNER TO postgres;
