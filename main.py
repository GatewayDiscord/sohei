#import sys
#sys.path.insert(0, os.path.abspath("..")) # this is for me to fix a local bug. not a part of the project itself.

from flask import Flask, flash, request, redirect, url_for, render_template, abort
from flask_sqlalchemy import SQLAlchemy
import json


app=Flask(__name__, template_folder="templates")
#app.config['SQLALCHEMY_DATABASE_URI']=="sqlite:///test.db"
#app.config['SECRET_KEY']="random string"
#db=SQLAlchemy(app)

configs=json.load(open('config.json'))


def input_sanity_check(text):
    sanitised=re.sub('[^a-zA-z0-9]', '', text)

    if sanitised==text:
        return [True, sanitised]
    else:
        return [False, sanitised]

@app.route('/')
def welcome():
    return render_template('index.html', team_name=configs["team_name"], head_text=configs["head_text"])

@app.route('/login', methods=["GET", "POST"])
def login():
        return render_template('login.html', team_name=configs["team_name"], head_text=configs["head_text"])

if __name__=="__main__":
    #Models.db.create_all()
    app.run(debug=True,host="127.0.0.1")


