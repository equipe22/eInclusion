from flask import Flask, render_template, request, url_for, flash, redirect
from scripts.interaction import interaction_einclusion
from scripts.modele_body import body_modele
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def hello():
    return '1234'