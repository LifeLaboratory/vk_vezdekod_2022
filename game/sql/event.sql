-- Table: public.event

-- DROP TABLE public.event;
CREATE SEQUENCE IF NOT EXISTS event_id_event_seq START 1;

CREATE TABLE IF NOT EXISTS public.event
(
  id_event integer NOT NULL DEFAULT nextval('event_id_event_seq'::regclass),
  description text,
  id_session text,
  round int DEFAULT 1,
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

INSERT INTO "event" ("id_event", "description", "id_session") VALUES
(1,	'сломался компьютер',	NULL),
(2,	'завис компьютер',	NULL),
(3,	'перегрелся и выключился',	NULL),
(4,	'сгорел монитор',	NULL),
(5,	'вылез winlocker, заблокировавший работу ПК',	NULL),
(6,	'вы сильно заболели и пришлось пойти в больницу',	NULL),
(7,	'на компьютере появился вирус.',	NULL),
(8,	'компьютер стал сильно зависать',	NULL),
(9,	'антивирус заблокировал все HTTP запросы',	NULL),
(10,	'данные компьютера зашифровались',	NULL),
(11,	'учётные данные утекли',	NULL),
(12,	'слишком простой пароль, хакер смог подобрать',	NULL),
(13,	'передача данных карты привела к краже денег с карты',	NULL),
(14,	'Ваши персональные данные утекли',	NULL);