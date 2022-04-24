-- Table: public.person

-- DROP TABLE public.person;

CREATE TABLE IF NOT EXISTS public.person
(
  id_person integer NOT NULL,
  name text,
  description text,
  pic text,
  health double precision,
  point double precision,
  money double precision,
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

INSERT INTO "person" ("id_person", "name", "description", "pic", "health", "point", "money", "communication", "value") VALUES
(2,	'Программист',	'Пишу бэки на Python, фронты на React, поднимаю на k8s и точно знаю как вести себя в интернете!',	'https://i1.wp.com/s3.amazonaws.com/gymndz/wp-content/uploads/2018/04/%D1%801.png?ssl=1',	75,	150,	300,	200,	205),
(1,	'Студент',	'Я только учусь, но уже разбираюсь во всех интернетах!',	'https://st.depositphotos.com/3526225/5170/v/600/depositphotos_51707511-stock-illustration-student-flat-illustration-with-icons.jpg',	100,	50,	150,	100,	100);
