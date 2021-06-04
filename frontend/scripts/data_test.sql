INSERT INTO patient (patient_id, firstname, lastname, date_of_birth) VALUES (1, 'f0', 'l0', '10/07/2004');
INSERT INTO patient (patient_id, firstname, lastname, date_of_birth) VALUES (10001, 'f1', 'l1', '14/07/1997');
INSERT INTO patient (patient_id, firstname, lastname, date_of_birth) VALUES (10002, 'f2', 'l2', '10/04/2011');
INSERT INTO patient (patient_id, firstname, lastname, date_of_birth) VALUES (10003, 'f3', 'l3', '03/03/2003');
INSERT INTO patient (patient_id, firstname, lastname, date_of_birth) VALUES (10004, 'f4', 'l4', '14/04/1954');

INSERT INTO studysource(studysource_id, study_source) VALUES (0, 'REDCAP');

INSERT INTO study (study_id, study_internalid, study_name, studysource_id) VALUES (11, 't1', 'test_study1', 0);
INSERT INTO study (study_id, study_internalid, study_name, studysource_id) VALUES (12, 't2', 'test_study2', 0);
INSERT INTO study (study_id, study_internalid, study_name, studysource_id) VALUES (13, 't3', 'test_study3', 0);

INSERT INTO patientstudy (patient_id, study_id, record_identifier) VALUES (10001, 11, '1');
INSERT INTO patientstudy (patient_id, study_id, record_identifier) VALUES (10002, 11, '2');
INSERT INTO patientstudy (patient_id, study_id, record_identifier) VALUES (10003, 12, '3');
INSERT INTO patientstudy (patient_id, study_id, record_identifier) VALUES (10004, 13, '4');