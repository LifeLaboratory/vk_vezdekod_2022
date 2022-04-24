CREATE TABLE IF NOT EXISTS images (
  id_image INT NOT NULL,
  link varchar(250) NOT NULL,
  author varchar(250) NOT NULL,
  likes INT NOT NULL,
  ord INT NOT NULL,
  time_stamp timestamp NOT NULL,
  PRIMARY KEY (id_image)
);

CREATE SEQUENCE IF NOT EXISTS history_id_history_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE IF NOT EXISTS history (
    "id_history" integer DEFAULT nextval('history_id_history_seq') NOT NULL,
    "id_image" integer NOT NULL,
    "time_stamp" timestamp NOT NULL,
    CONSTRAINT "history_pkey" PRIMARY KEY ("id_history")s
);
