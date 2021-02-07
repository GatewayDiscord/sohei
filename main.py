import os
import sys
sys.path.insert(0, os.path.abspath("..")) # this is for me to fix a local bug. not a part of the project itself.

from flask import Flask, flash, request, redirect, url_for, render_template, abort, session
from flask_sqlalchemy import SQLAlchemy
from sohei import Models
from functools import wraps
import secrets
import time
import re
import string
import bcrypt
import json


app=Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(200))
db=SQLAlchemy(app)


salt = b"$2a$12$w40nlebw3XyoZ5Cqke14M." #look into the security side of things with this

configs=json.load(open('config.json'))


def restricted(access_level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                username=session['username']
            except:
                abort(403)

            user_=Models.Users.query.filter_by(username=username).first()
            if user_.role==access_level or user_.role=="admin":
                return func(*args, **kwargs)
            else:
                abort(403)
        return wrapper
    return decorator


def sanitise(text):
    sanitised=re.sub('[^a-zA-z0-9]', '', str(text))
    sanitised.replace(' ','')

    if sanitised==text:
        return [True, sanitised]
    else:
        return [False, sanitised]

def register(username, password, role):
    username=sanitise(username)[1]
    password=bcrypt.hashpw(password.encode(), salt)
    role=sanitise(role)[1]
    User=Models.Users.query.filter_by(username=username).first()
    if User is None:
        new_user=Models.Users(username, password, time.strftime("%A %B, %d %Y %H:%M:%S"), role)
        Models.db.session.merge(new_user)
        Models.db.session.commit()
        return "Success"
    else:
        return "User already exists"

@app.route('/')
def welcome():
    return render_template('index.html', team_name=configs["team_name"], head_text=configs["head_text"])


@app.route('/login', methods=["GET", "POST"])
def login():
    error=""

    try:
        username=request.form['username']
        password=request.form['password']

        if username=="":
            print('username is none')
        elif sanitise(username)[0]==False:
            print('username doesn\'t exist.')
            error="Username doesn't exist."
        else:
            try:
                user=Models.Users.query.filter_by(username=sanitise(username)[1]).first()
            except Exception as e:
                print(e)
            if user is not None:
                hashed_password=bcrypt.hashpw(password.encode(), salt)
                if user.password==hashed_password:
                    session['username']=username
                    session['role']=user.role
                    return redirect(url_for('.challenges'))
                else:
                    error="Username or password is incorrect."
            else:
                error="Username or password is incorrect."
    except Exception as e:
        print(e)
        return render_template('login.html', team_name=configs["team_name"], head_text=configs["head_text"], error=error)
    return render_template('login.html', team_name=configs["team_name"], head_text=configs["head_text"], error=error)


@app.route('/admin', methods=["GET","POST"])
@restricted('admin')
def admin_index():
    return render_template("admin_index.html",team_name=configs["team_name"], head_text=configs["head_text"])


@app.route('/admin/adduser', methods=['GET',"POST"])
@restricted('admin')
def adduser():
    error=""
    try:
        if request.form["username"]!="" and request.form["password"]!="" and request.form["role"]!="":
            res=register(request.form["username"], request.form["password"], request.form["role"])
            if res=="Success":
                error=f"User {sanitise(request.form['username'])[1]} registered." #more like a success message but i utilised it anyway
            else:
                error=f"User {sanitise(request.form['username'])[1]} already exists."
    except Exception as e:
        print(e)
    return render_template('adduser.html',team_name=configs["team_name"], head_text=configs["head_text"], error=error)


@app.route('/challenges', methods=["GET","POST"])
@restricted('member')
def challenges():
    return f"Logged in as {session['username']} with role {session['role']}"

if __name__=="__main__":
    #Models.db.create_all() #setup.py takes care of that.
    app.run(debug=True,host="127.0.0.1")
