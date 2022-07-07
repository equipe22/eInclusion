# -*- coding: utf-8 -*-
"""
Created 2022/07/05

@author: David BAUDOIN

fonction : crétion de la base de donnees eInclusion

input : DB_Einclusion.sql, db_config
Etape :
    -lecture et recuperation de chaque requete de creation
    -application et verification de chaque requete
"""
import os, pprint, argparse
from scripts.DB_connector import DB_Einclusion


def setup (dic_config, DBfile_sql):
    f_dbrequest = open(DBfile_sql, 'r')
    text_DB = f_dbrequest.read()

    list_request = []
    for request in text_DB.split(';').replace('\n',''):
        if len(request)>2:
            list_request.append(request)





def main(DB_file, DB_config):
    # DB parameters
    dic_config = {}
    f_db_config = open(DB_config, 'r')
    for line in f_db_config:
        dic_config[line.split('=')[0]] = line.split('=')[1].replace('\n', '')

    #search_redcap_data(dic_db_param['api_url'], dic_db_param['api_key'])
    setup(dic_config, DB_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--DB_file", help="input file for create DB")
    parser.add_argument("--DB_config", help="file of config DB server")
    args = parser.parse_args()
    if args.directory:
        print("Go with the inputFolder")
        main(args.DB_file, args.DB_config)