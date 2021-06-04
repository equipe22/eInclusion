CREATE TABLE "patient" (
  "patient_id" SERIAL PRIMARY KEY,
  "ipp" varchar(20),
  "firstname" varchar,
  "lastname" varchar,
  "date_of_birth" varchar,
  "date_of_death" varchar
);

CREATE TABLE "studysource" (
  "studysource_id" int PRIMARY KEY,
  "study_source" varchar NOT NULL
);

CREATE TABLE "study" (
  "study_id" int PRIMARY KEY,
  "study_internalid" varchar(100),
  "study_name" varchar(100),
  "studysource_id" int NOT NULL
);

CREATE TABLE "patientstudy" (
  "patient_id" int,
  "study_id" int,
  "record_identifier" varchar
);

ALTER TABLE "patientstudy" ADD PRIMARY KEY ("patient_id", "study_id");

CREATE TABLE "provider" (
  "provider_id" int PRIMARY KEY,
  "provider_name" varchar
);

CREATE TABLE "patientprovider" (
  "patient_id" int,
  "provider_id" int
);

ALTER TABLE "patientprovider" ADD PRIMARY KEY ("patient_id", "provider_id");

CREATE TABLE "user" (
  "user_id" int PRIMARY KEY,
  "user_name" varchar
);

CREATE TABLE "user_aliases" (
  "user_id" int,
  "user_alias" varchar
);

CREATE TABLE "userprovider" (
  "user_id" int,
  "provider_id" int
);

CREATE TABLE "userstudy" (
  "user_id" int,
  "study_id" int
);

ALTER TABLE "userprovider" ADD PRIMARY KEY ("user_id", "provider_id");

CREATE TABLE "log" (
  "user_id" int,
  "action" int,
  "patient_id" int,
  "timestamp" timestamp
);

ALTER TABLE "study" ADD FOREIGN KEY ("studysource_id") REFERENCES "studysource" ("studysource_id");

ALTER TABLE "patientstudy" ADD FOREIGN KEY ("patient_id") REFERENCES "patient" ("patient_id");

ALTER TABLE "patientstudy" ADD FOREIGN KEY ("study_id") REFERENCES "study" ("study_id");

ALTER TABLE "patientprovider" ADD FOREIGN KEY ("patient_id") REFERENCES "patient" ("patient_id");

ALTER TABLE "patientprovider" ADD FOREIGN KEY ("provider_id") REFERENCES "provider" ("provider_id");

ALTER TABLE "user_aliases" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "userprovider" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "userprovider" ADD FOREIGN KEY ("provider_id") REFERENCES "provider" ("provider_id");



