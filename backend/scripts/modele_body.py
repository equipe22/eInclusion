# -*- coding: utf-8 -*-
"""
Created 2020/10/05

@author: David BAUDOIN

fonction : modele d'entree des informations
"""

class body_modele:
    def __init__(self, ipp='', firstname='', lastname='', study_name='', study_id='', source='', record_id='', datebirth='', user_id = ''):
        self.ipp = ipp
        self.lastname = lastname
        self.firstname = firstname
        self.study_name = study_name
        self.study_id = study_id
        self.source = source
        self.record_id = record_id
        self.datebirth = datebirth
        self.user_id = user_id

    def write_patient_info_into_body(self, ipp='', firstname='', lastname='', record_id=''):
        self.ipp = ipp
        self.lastname = lastname
        self.firstname = firstname
        self.record_id = record_id

    def write_study_info_into_body(self, study_name='', study_id='', source=''):
        self.study_name = study_name
        self.study_id = study_id
        self.source = source