# -*- coding: utf-8 -*-
"""
Created 2020/10/10

@author: David BAUDOIN

fonction : script de transformation des donnees csv (ac une ligne titre) en ligne insert sql

"""
import sys

def setup(file_csv, sep, file_sql):
    f_csv = open(file_csv, 'r')
    titles = f_csv.readline()
    f_sql = open (file_sql, 'w')

    sql_request_base = 'INSERT INTO ces ('
    for title in titles.split(sep) :
        sql_request_base += title + ', '
    sql_request_base = sql_request_base[:-2] + ') VALUES ('

    for line in f_csv:
        sql_request_data = ''
        for data in line.split(sep): sql_request_data += '"' + data.replace('"', '') + '", '
        request = sql_request_base + sql_request_data [:-2] + ');'
        f_sql.write(request)
        f_sql.write('\n')
        print(request)

def main():
    file_csv = sys.argv[1]
    sep = sys.argv[2]
    file_sql = sys.argv[3]

    setup(file_csv, sep, file_sql)

if __name__ == '__main__':
    main()