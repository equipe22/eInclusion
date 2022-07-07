DROP DATABASE IF EXISTS  einclusion;
CREATE DATABASE einclusion;

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
  "user_id" varchar,
  "user_alias" varchar
);

CREATE TABLE "userprovider" (
  "user_id" varchar,
  "provider_id" int
);

CREATE TABLE "userstudy" (
  "user_id" varchar,
  "study_id" int
);

ALTER TABLE "userprovider" ADD PRIMARY KEY ("user_id", "provider_id");

CREATE TABLE "log" (
  "user_id" varchar,
  "action" int,
  "patient_id" int,
  "timestamp" timestamp
);
