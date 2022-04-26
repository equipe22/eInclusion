from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, send_file, g
from werkzeug.exceptions import abort
from urllib.request import urlopen
from scripts.export_xls import export_data_to_excel
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
ipp_server_port = '10.149.219.161:5000'
current_study = {}


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Hello, It\'s Frontend Einclusion!'

@app.route('/list_study')
def index():
    current_study['now'] = '0'
    #0 recuperation des informations dans einclusion de la liste de projets present
    with urlopen('http://'+ipp_server_port+'/list_study') as r:
        dataset = r.read()

    #1 traitement sur les donnees recu
    #print(dataset)
    informations = []
    for data in dataset.decode('utf-8').replace('[', '').replace(']', '').split('), ('):
        #print(data)
        result = {}
        result['id'] = data.replace('(', '').replace(')', '').split(', ')[0].replace('\'', '')
        result['idRedcap'] = data.replace('(', '').replace(')', '').split(', ')[1].replace('\'', '')
        result['study_name'] = data.replace('(', '').replace(')', '').split(', ')[2].replace('\'', '')
        result['sourcesystem'] = data.replace('(', '').replace(')', '').split(', ')[3].replace('\'', '')
        result['resultPatient'] = data.replace('(', '').replace(')', '').split(', ')[4].replace('\'', '')
        informations.append(result)

    #2 generation de la page web
    return render_template('index.html', posts=informations)
    #return dataset

@app.route("/export/", methods=['POST'])
def export_csv():
    #Moving forward code
    forward_message = "Moving Forward..."
    data_test = {'first':[2, 2], 'second':[3, 3]}
    # 0 recuperation des informations dans einclusion de la liste de projets present
    with urlopen('http://'+ipp_server_port+'/list_study') as r:
        dataset = r.read()

    # maniment du dataset en dictionnaire
    data_xls = {}
    data_xls['id'] = []
    data_xls['idRedcap'] = []
    data_xls['study_name'] = []
    data_xls['sourcesystem'] = []
    data_xls['resultPatient'] = []

    for data in dataset.decode('utf-8').replace('[', '').replace(']', '').split('), ('):
        data_xls['id'].append(data.replace('(', '').replace(')', '').split(', ')[0].replace('\'', ''))
        data_xls['idRedcap'].append(data.replace('(', '').replace(')', '').split(', ')[1].replace('\'', ''))
        data_xls['study_name'].append(data.replace('(', '').replace(')', '').split(', ')[2].replace('\'', ''))
        data_xls['sourcesystem'].append(data.replace('(', '').replace(')', '').split(', ')[3].replace('\'', ''))
        data_xls['resultPatient'].append(data.replace('(', '').replace(')', '').split(', ')[4].replace('\'', ''))

    output = export_data_to_excel(data=data_xls)
    return send_file(output, attachment_filename="testing"+datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+".xlsx", as_attachment=True)


@app.route("/export_study/", methods=['POST'])
def export_csv_study():
    #Moving forward code
    # 0 recuperation des informations dans einclusion de la liste de projets present
    with urlopen('http://'+ipp_server_port+'/info_study/'+current_study['now']) as r:
        dataset = r.read()

    # maniment du dataset en dictionnaire
    data_xls = {}
    data_xls['record_id'] = []
    data_xls['IPP'] = []
    data_xls['firstname'] = []
    data_xls['lastname'] = []
    data_xls['date of birth'] = []

    for data in dataset.decode('utf-8').replace('[', '').replace(']', '').split('), ('):
        data_xls['record_id'].append(data.replace('(', '').replace(')', '').split(', ')[0].replace('\'', ''))
        data_xls['IPP'].append(data.replace('(', '').replace(')', '').split(', ')[1].replace('\'', ''))
        data_xls['firstname'].append(data.replace('(', '').replace(')', '').split(', ')[2].replace('\'', ''))
        data_xls['lastname'].append(data.replace('(', '').replace(')', '').split(', ')[3].replace('\'', ''))
        data_xls['date of birth'].append(data.replace('(', '').replace(')', '').split(', ')[4].replace('\'', ''))

    output = export_data_to_excel(data=data_xls)
    return send_file(output, attachment_filename="info_study"+current_study['now']+datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+".xlsx", as_attachment=True)

@app.route('/study/<string:study_id>', methods=['GET', 'POST'])
def studypage(study_id):
    # 0 recuperation des informations dans einclusion de la liste de projets present
    current_study['now'] = str(study_id)
    with urlopen('http://'+ipp_server_port+'/info_study/'+study_id) as r:
        dataset = r.read()
    # 1 traitement sur les donnees recu
    print(dataset)
    informations = []
    for data in dataset.decode('utf-8').replace('[', '').replace(']', '').split('), ('):
        print(data)
        result = {}
        result['patient_id'] = data.replace('(', '').replace(')', '').split(', ')[0].replace('\'', '')
        result['nip'] = data.replace('(', '').replace(')', '').split(', ')[1].replace('\'', '')
        result['firstname'] = data.replace('(', '').replace(')', '').split(', ')[2].replace('\'', '')
        result['lastname'] = data.replace('(', '').replace(')', '').split(', ')[3].replace('\'', '')
        result['dob'] = data.replace('(', '').replace(')', '').split(', ')[4].replace('\'', '')
        result['sourcesystem'] = data.replace('(', '').replace(')', '').split(', ')[5].replace('\'', '')
        informations.append(result)
    return render_template('post.html', posts=informations)

@app.route('/addpatienttostudy/', methods=['GET', 'POST'])
def add_patient_in_study(study_id):
    # Moving to create patient
    forward_message = "Moving Forward..."
    return render_template('addpatient.html', forward_message=forward_message)

@app.route('/userinfo/<string:user_id>', methods=['GET', 'POST'])
def userinfo(user_id):
    # 0 recuperation des informations dans einclusion de la liste de projets present
    with urlopen('http://'+ipp_server_port+'/info_study/'+user_id) as r:
        dataset = r.read()
    # 1 traitement sur les donnees recu
    print(dataset)
    informations = []
    for data in dataset.decode('utf-8').replace('[', '').replace(']', '').split('), ('):
        print(data)
        result = {}
        result['patient_id'] = data.replace('(', '').replace(')', '').split(', ')[0].replace('\'', '')
        result['nip'] = data.replace('(', '').replace(')', '').split(', ')[1].replace('\'', '')
        result['firstname'] = data.replace('(', '').replace(')', '').split(', ')[2].replace('\'', '')
        result['lastname'] = data.replace('(', '').replace(')', '').split(', ')[3].replace('\'', '')
        result['dob'] = data.replace('(', '').replace(')', '').split(', ')[4].replace('\'', '')
        result['sourcesystem'] = data.replace('(', '').replace(')', '').split(', ')[5].replace('\'', '')
        informations.append(result)
    return render_template('post.html', posts=informations)