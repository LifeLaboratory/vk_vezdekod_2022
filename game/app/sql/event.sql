-- Table: public.event

-- DROP TABLE public.event;

CREATE TABLE IF NOT EXISTS public.event
(
  id_event integer NOT NULL DEFAULT nextval('event_id_event_seq'::regclass),
  description text,
  id_session text,
  CONSTRAINT event_pk PRIMARY KEY (id_event)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.event
  OWNER TO postgres;

-- Index: public.event_id_event_uindex

-- DROP INDEX public.event_id_event_uindex;

CREATE UNIQUE INDEX IF NOT EXISTS event_id_event_uindex
  ON public.event
  USING btree
  (id_event);

