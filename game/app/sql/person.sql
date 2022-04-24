-- Table: public.person

-- DROP TABLE public.person;

CREATE TABLE IF NOT EXISTS public.person
(
  id_person integer NOT NULL,
  name text,
  description text,
  pic text,
  health double precision,
  food double precision,
  leisure double precision,
  communication double precision,
  value integer,
  CONSTRAINT person_pk PRIMARY KEY (id_person)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.person
  OWNER TO postgres;

-- Index: public.person_id_person_uindex

-- DROP INDEX public.person_id_person_uindex;

CREATE UNIQUE INDEX IF NOT EXISTS person_id_person_uindex
  ON public.person
  USING btree
  (id_person);

