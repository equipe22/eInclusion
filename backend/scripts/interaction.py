"""
script d'interaction entre la base de donnee einclusion et les resultats d'appel redcap

"""
from scripts.DB_connector import DB_Einclusion

class interaction_einclusion:
    def __init__(self):
        self.connector_einclusion = DB_Einclusion()

    def redcap_add_study(self, study_id, study_name):
        self.connector_einclusion.insert_study(str(study_id), study_name)
        print('add study ' + str(study_id) + ' : ' + study_name)

    def redcap_update_patient(self, info_patient, body):
        id_patient = info_patient[0][0]
        if body.firstname != '': self.connector_einclusion.update_patient(id_patient, 'firstname', body.firstname)
        if body.lastname != '': self.connector_einclusion.update_patient(id_patient, 'lastname', body.lastname)
        if body.datebirth != '': self.connector_einclusion.update_patient(id_patient, 'date_of_birth', body.datebirth)
        if body.ipp != '': self.connector_einclusion.update_patient(id_patient, 'ipp', body.ipp)
        self.connector_einclusion.delete_linf_patient(body.study_id, body.record_id)
        self.connector_einclusion.insert_link_patient_study(info_patient[0][0], body.study_id, body.record_id)

    def redcap_add_patient(self, ipp, fname, lname, dob, study_id, user_id, record_id):
        self.connector_einclusion.insert_patient(ipp, firstname=fname, lastname=lname, dob=dob)
        print('patient : ' + str(ipp) + ' added to study')
        info_patient = self.connector_einclusion.find_patient_by_ipp(ipp)
        print(info_patient)
        self.connector_einclusion.insert_link_patient_study(info_patient[0][0], study_id, record_id)

    def search_patient(self, body):
        check_user = self.connector_einclusion
        if check_user:
            res = self.connector_einclusion.search_patient_in_study(source=body.source, study_id=body.study_id, record_id=body.record_id)
            if res == []:
                print('failed to find patient')
            return res
        else:
            return 'failed to find patient'

    def search_patient_id(self, body):
        check_user = self.connector_einclusion
        if check_user and body.record_id != '':
            res = self.connector_einclusion.find_patient(record_id=body.record_id, study_id=body.study_id)
            if res == []: return ['', '', '', '']
            else : return res
        else:
            return ['', '', '', '']

    def call_add_patient_ipp(self, body):
        #check if user exist and create if not exist
        id_user = '0'
        '''
        if body.user_id == None :
            body.user_id = 0
        id_user = self.connector_einclusion.search_user(body.user_id)
        if id_user == '':
            id_user = self.connector_einclusion.search_last_user()
            self.connector_einclusion.insert_user(id_user, body.user_id)
        '''
        ###############################################
        #check if study exist
        check_study = self.connector_einclusion.check_study(body.study_id)
        if not check_study:
            self.redcap_add_study(body.study_id, body.study_name)
        #link study to user
        if not self.connector_einclusion.check_link_user_study(id_user, body.study_id):
            self.connector_einclusion.insert_user_study_link(id_user, body.study_id)
        ###############################################
        info_patient = self.connector_einclusion.find_patient_by_record_id(body.record_id, body.study_id)
        if info_patient == []:
            self.redcap_add_patient(body.ipp, body.firstname, body.lastname, body.datebirth, body.study_id, body.user_id, body.record_id)
        else: self.redcap_update_patient(info_patient, body)

    def list_Einclusion_in_list_study(self):
        data = self.connector_einclusion.search_list_study()
        return data

    def list_Einclusion_info_study(self, study_id):
        data = self.connector_einclusion.search_all_patients_in_study(study_id)
        return data