from flask import render_template, request, redirect, url_for, flash, Response

#? Flask App
from __init__ import my_app

#? Auth
from flask_login import current_user, login_user, logout_user, login_required, UserMixin

#? DB 
from __init__ import my_db
from models import *

#? Mail
from __init__ import my_mail



TOKEN_EXPIRY = 15 * 60  # Token expires in 60 secs


#? API Endpoints

@my_app.route('/')
def home():
    return render_template('home.html', title='Home')