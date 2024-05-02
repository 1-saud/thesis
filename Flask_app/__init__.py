from flask import Flask

#? Model
from flask_sqlalchemy import SQLAlchemy

#? Auth
from flask_login import LoginManager

#? Emails
from flask_mail import Mail

#? Admin Dashboard 
from flask_admin import Admin


#? Optimizations
# from flask_pure import Pure
from flask_compress import Compress
from flask_caching import Cache


def create_app():
    #? Configuration
    app = Flask(__name__, static_folder="static/")

    # Server Deployment
    # Only for Heroku deployment
    #app.config['SERVER_ADDRESS'] = 'https://tutoring.herokuapp.com/'
    app.config['SECRET_KEY'] = b'\xea]\x1c\x84\xf0\xc2\xce\xd1\x1al\xbd\xd4'

    #? DB Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    
    #? Admin Dashboard
    admin = Admin(app)

    #? Auth
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    #? Flask mail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465  # Your email ID here
    
    # One last thing, google, by default, restricts bots to send mails or something for security purposes.
    
    # email here 
    app.config['MAIL_USERNAME'] = app.config['MAIL_DEFAULT_SENDER'] = 'noreply.tutoring.team@gmail.com'
    
    # So you'll have to go to this website https://myaccount.google.com/lesssecureapps from the Google id you'll use for emails and give access.
    app.config['MAIL_PASSWORD'] = 'Mr.NoReply.tutoring-3002'  # ? Your password here
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail = Mail(app)
    
    #? Optimizations
    app, cache = flask_optimize(app)
    
    return app, cache, db, admin, mail, login_manager


def flask_optimize(app):
    #? CSS
    # app.config["PURECSS_RESPONSIVE_GRIDS"] = True
    # app.config["PURECSS_USE_CDN"] = True
    # app.config["PURECSS_USE_MINIFIED"] = True
    # Pure(app)
    
    #? Gzip Compression 
    Compress(app)  
    
    #? Simple in-memory cache
    app.config["CACHE_TYPE"] = "simple"  # Use a simple in-memory cache
    app.config[
        "CACHE_DEFAULT_TIMEOUT"
    ] = 300  # Set the default cache timeout in seconds (e.g., 300 seconds = 5 minutes)

    cache = Cache(app) 
    
    return app, cache


def jinja_opt(app):
    "If needed call this app = jinja_opt(app) to modify jinja delimiters"
    
    #? Change Jinja2 delimiters for variable expressions
    app.jinja_options = app.jinja_options.copy()
    app.jinja_options['variable_start_string'] = '[['
    app.jinja_options['variable_end_string'] = ']]'

    #? Change Jinja2 delimiters for control structures
    app.jinja_options['block_start_string'] = '[%'
    app.jinja_options['block_end_string'] = '%]'

    #? Change Jinja2 delimiters for comments
    app.jinja_options['comment_start_string'] = '[#'
    app.jinja_options['comment_end_string'] = '#]'
    
    return app


#! Will be called in app.py to start flask server (& imported by other modules)
my_app, my_cache, my_db, my_admin, my_mail, my_login_manager = create_app()
