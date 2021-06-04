from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from scripts.interaction import interaction_einclusion
from scripts.modele_body import body_modele
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    einclusion = interaction_einclusion()
    body = body_modele(study_id='11', source='redcap', record_id='10001')
    research = einclusion.search_patient(body=body)
    print(research)
    return render_template('index.html', posts=research)
'''
@app.route('/ipp/<string:post_id>')
def post(post_id):
    post = {}
    einclusion = interaction_einclusion()
    body = body_modele(ipp=str(post_id))
    res = einclusion.search_patient_id(body)
    print(res)
    try:
        post['title'] = 'find patient'
        post['firstname'] = res[0]
        post['lastname'] = res[1]
        post['date_of_birth'] = res[2]
        post['nip'] = res[3]
        return post['nip']
        #return render_template('post.html', post=post)

    except:
        post['title'] = 'find patient'
        post['firstname'] = ''
        post['lastname'] = ''
        post['date_of_birth'] = ''
        return ''
        #return render_template('post.html', post=post)
'''
@app.route('/ipp/<string:record_id>/<string:study_id>')
def post(record_id, study_id):
    post = {}
    einclusion = interaction_einclusion()
    body = body_modele(record_id=str(record_id), study_id=str(study_id))
    res = einclusion.search_patient_id(body)
    try:
        post['title'] = 'find patient'
        post['nip'] = res[3]
        return post['nip']

    except:
        post['title'] = 'find patient'
        return ''

@app.route('/list_study')
def data_list_study():
    einclusion = interaction_einclusion()
    data = einclusion.list_Einclusion_in_list_study()
    print(data)
    return str(data)

@app.route('/info_study/<string:study_id>')
def data_info_study(study_id):
    einclusion = interaction_einclusion()
    data = einclusion.list_Einclusion_info_study(study_id)
    print(data)
    return str(data)

@app.route('/firstname/<string:record_id>/<string:study_id>')
def firstname(record_id, study_id):
    post = {}
    einclusion = interaction_einclusion()
    body = body_modele(record_id=str(record_id), study_id=str(study_id))
    res = einclusion.search_patient_id(body)
    try:
        post['title'] = 'find patient'
        post['firstname'] = res[0]
        return post['firstname']

    except:
        post['title'] = 'find patient'
        return ''

@app.route('/lastname/<string:record_id>/<string:study_id>')
def lastname(record_id, study_id):
    post = {}
    einclusion = interaction_einclusion()
    body = body_modele(record_id=str(record_id), study_id=str(study_id))
    res = einclusion.search_patient_id(body)
    try:
        post['title'] = 'find patient'
        post['lastname'] = res[1]
        return post['lastname']

    except:
        post['title'] = 'find patient'
        return ''

@app.route('/dateofbirth/<string:record_id>/<string:study_id>')
def dateofbirth(record_id, study_id):
    post = {}
    einclusion = interaction_einclusion()
    body = body_modele(record_id=str(record_id), study_id=str(study_id))
    res = einclusion.search_patient_id(body)
    try:
        post['title'] = 'find patient'
        post['date_of_birth'] = res[2]
        return post['date_of_birth']

    except:
        post['title'] = 'find patient'
        return ''

@app.route('/identification/nip/', methods=['POST'])
def transfert_identity():
    body = body_modele(lastname=str(request.form.to_dict()['lastname']),
                       source=str(request.form.to_dict()['source']),
                       record_id=str(request.form.to_dict()['record']),
                       firstname=str(request.form.to_dict()['firstname']),
                       datebirth=str(request.form.to_dict()['date_of_birth']),
                       ipp=str(request.form.to_dict()['ipp']),
                       user_id=str(request.form.to_dict()['user']),
                       study_id=str(request.form.to_dict()['project']))
    einclusion = interaction_einclusion()
    einclusion.call_add_patient_ipp(body)
    print(request.form.to_dict())
    #for data in request.form.to_dict(): print('key : ' + str(data) + '  data : ' + str(request.form.to_dict()[data]))
    return ''

@app.route('/<string:name>/<string:firstname>/<string:datebirth>/<string:ipp>/<string:record_id>/<string:study_id>')
def find_nume_patient(name, firstname, datebirth, ipp, record_id, study_id):
    einclusion = interaction_einclusion()
    body = body_modele(lastname=name, source='redcap', record_id=record_id, firstname=firstname, datebirth=datebirth, ipp=ipp, study_id=study_id)
    einclusion.call_add_patient_ipp(body)
    return ''

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

