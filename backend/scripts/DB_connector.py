# -*- coding: utf-8 -*-
"""
Created 2020/10/05

@author: David BAUDOIN

fonction : script d'interaction avec la base de donnees einclusion

"""

import psycopg2

class DB_Einclusion:

    # construction de l'objet
    def __init__(self):
        self.DB_host = 'localhost'
        self.DB_name = 'einclusion'
        self.DB_port = '5433'
        self.DB_user = 'postgres'
        self.DB_password = 'postgres'
        self.dbcon = None

    def connect(self):
        config = 'host=' + self.DB_host + ' port=' + self.DB_port + ' dbname=' + self.DB_name + ' user=' + self.DB_user + ' password=' + self.DB_password
        self.dbcon = psycopg2.connect(config)
        self.dbcon.autocommit = True
        cur = self.dbcon.cursor()
        return cur

    def insert_patient(self, ipp, firstname='', lastname='', dob=''):
        cursor = self.connect()
        request = 'insert into patient (firstname, lastname, ipp, date_of_birth) values '
        request += '(\'' + firstname + '\', \'' + lastname +'\', \'' + ipp + '\', \'' + dob + '\')'
        print(request)
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def insert_link_patient_study(self, patient_id, study_id, record_id):
        cursor = self.connect()
        request = 'insert into patientstudy (patient_id, study_id, record_identifier) values '
        request += '(' + patient_id + ' ,' + study_id + ', \'' + record_id + '\')'
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def find_patient(self, record_id, study_id):
        res = []
        cursor = self.connect()
        request = 'select p.firstname, p.lastname, p.date_of_birth, p.ipp from patient p, patientstudy ps '
        request += 'where ps.record_identifier = \'' + record_id + '\' and ps.study_id = ' + study_id + ' and ps.patient_id = p.patient_id'
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            tuple_resp = []
            for data in row:
                tuple_resp.append(str(data))
            res.append(tuple_resp)
        cursor.close()
        if len(res) == 0: return []
        return res[0]

    def find_patient_by_ipp(self, ipp):
        res = []
        cursor = self.connect()
        request = 'select patient_id, firstname, lastname, date_of_birth from patient where ipp = \'' + ipp + '\''
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            tuple_resp = []
            for data in row:
                tuple_resp.append(str(data))
            res.append(tuple_resp)
        cursor.close()
        return res

    def find_patient_by_record_id(self, record_id, study_id):
        res = []
        cursor = self.connect()
        request = 'select p.patient_id, p.firstname, p.lastname, p.date_of_birth from patient p, patientStudy ps where ps.record_identifier = \'' + record_id + '\''
        request += 'and study_id = \'' + study_id + '\''
        request += 'and ps.patient_id = p.patient_id'
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            tuple_resp = []
            for data in row:
                tuple_resp.append(str(data))
            res.append(tuple_resp)
        cursor.close()
        return res

    def find_last_record_id(self, study_id):
        cursor = self.connect()
        request = 'select MAX(ps.record_identifier) from patient p, patientStudy ps '
        request += 'where study_id = \'' + study_id + '\' '
        request += 'and length(ps.record_identifier) = (select MAX(length(ps.record_identifier)) from patientStudy ps where study_id = \''+study_id+'\')'
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            for data in row:
                return data[0]
        cursor.close()
        return ''

    def update_patient(self,id_patient, varname, value):
        cursor = self.connect()
        request = 'update patient set ' + varname + ' = \'' + value + '\' where patient_id = ' + id_patient
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def check_study(self, study_id):
        res = False
        cursor = self.connect()
        request = 'select * from study where study_id = ' + study_id
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            res = True
            break
        cursor.close()
        return res

    def insert_study(self, study_id, study_name):
        cursor = self.connect()
        request = 'insert into study (study_id, study_name, studysource_id) values '
        request += '(' + study_id + ', \'' + study_name + '\', 0)'
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def search_patient_in_study(self, source, study_id, record_id):
        cursor = self.connect()
        res = []
        request = 'select p.patient_id, p.firstname, p.lastname, p.ipp from patient p, patientStudy ps where ps.study_id = ' + study_id
        request += 'and ps.patient_id = p.patient_id'
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            res.append(row)
            break
        cursor.close()
        return res

    def search_all_patients_in_study(self, study_id):
        cursor = self.connect()
        res = []
        request = 'select ps.record_identifier, p.ipp, p.firstname, p.lastname, p.date_of_birth, s.studysource_id '
        request += 'from patient p, patientStudy ps, study s '
        request += 'where ps.study_id = ' + study_id + ' and ps.patient_id = p.patient_id and s.study_id = ps.study_id'
        cursor.execute(request.encode('utf-8'))
        list_patient = []
        for row in cursor:
            list_patient.append(row)
        cursor.close()
        return list_patient

    def search_list_patient_in_study(self, study_id):
        cursor = self.connect()
        request = 'select * from patientStudy ps, patient p where ps.patient_id = p.patient_id and ps.study_id = ' + study_id
        cursor.execute(request.encode('utf-8'))
        list_patient = []
        for row in cursor:
            list_patient.append(row)
        cursor.close()
        return list_patient

    def delete_linf_patient(self, study_id, record_id):
        cursor = self.connect()
        request = 'delete from patientstudy where study_id = ' + study_id + ' and record_identifier = \'' + record_id +'\''
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def check_user_authorisation(self, user_id, study_id):
        res = False
        cursor = self.connect()
        request = 'select * from userStudy where study_id = ' + study_id + ' and user_id = ' + user_id
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            res = True
            break
        cursor.close()
        return res

    def search_list_study(self):
        cursor = self.connect()
        request = 'select s.study_id, s.study_internalid, s.study_name, s.studysource_id, countpatient.nb_patient '
        request += 'from study s, (select study_id, count(patient_id) nb_patient from patientstudy group by study_id) as countpatient '
        request += 'where s.study_id = countpatient.study_id'
        cursor.execute(request.encode('utf-8'))
        list_study = []
        for row in cursor:
            list_study.append(row)
        cursor.close()
        return list_study

    def insert_user(self, user_id, user_name):
        cursor = self.connect()
        request = 'insert into userapp (user_id, user_name) values '
        request += '(' +user_id + ', \''+user_name+'\') ON CONFLICT (user_id) DO NOTHING'
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def check_link_user_study(self, user_id, study_id):
        cursor = self.connect()
        request = 'select * from userstudy where user_id = \''+str(user_id)+'\' and study_id = '+str(study_id)
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            cursor.close()
            return True
        cursor.close()
        return False


    def insert_user_study_link (self, user_id, study_id):
        cursor = self.connect()
        request = 'insert into userstudy (user_id, study_id) values '
        request += '(\'' + user_id + '\', ' + study_id + ') '
        cursor.execute(request.encode('utf-8'))
        cursor.close()

    def search_last_user(self):
        result = 0
        cursor = self.connect()
        request = 'select MAX(user_id) from userapp'
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            result = row[0]
        return result

    def search_user(self, user_name):
        result = 0
        cursor = self.connect()
        request = 'select user_id from userapp'
        cursor.execute(request.encode('utf-8'))

    def send_last_userid(self):
        result = 0
        cursor = self.connect()
        request = 'select MAX(user_id) from userapp'
        cursor.execute(request.encode('utf-8'))
        for row in cursor:
            result = row
        return result