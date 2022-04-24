-- Table: public.session

-- DROP TABLE public.session;

CREATE TABLE IF NOT EXISTS public.session
(
  id_user integer,
  id_session text
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.session
  OWNER TO postgres;
