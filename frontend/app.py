from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from werkzeug.exceptions import abort
from urllib.request import urlopen

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Hello, It\'s Frontend Einclusion!'

@app.route('/list_study')
def index():
    #0 recuperation des informations dans einclusion de la liste de projets present
    with urlopen('http://10.149.219.161:5000/list_study') as r:
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


@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message)

@app.route('/study/<string:study_id>', methods=['GET', 'POST'])
def studypage(study_id):
    # 0 recuperation des informations dans einclusion de la liste de projets present
    with urlopen('http://10.149.219.161:5000/info_study/'+study_id) as r:
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
    with urlopen('http://10.149.219.161:5000/info_study/'+user_id) as r:
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