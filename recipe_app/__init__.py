#main __init__
import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


from config import Config

app = Flask(__name__)

app.config.from_object(Config)

##################

### DATABASE SETUPS ############

basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


######### db ###################

db = SQLAlchemy(app)
Migrate(app,db)

migrate = Migrate()

#### LOGIN CONFIGS #######

login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"

#### email support #######
mail = Mail(app)

######################################

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    return app

########################


#### BLUEPRINT CONFIGS STARTS #######
 
from recipe_app.core.views import core
from recipe_app.error_pages.handlers import error_pages
from recipe_app.users.views import users
from recipe_app.recipe_posts.views import recipe_posts


# Register the apps

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(recipe_posts)


#### BLUEPRINT CONFIGS END #######

############################# Debugging ##############################

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Recipe-site-failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


if not os.path.exists('logs'):
	os.mkdir('logs')

file_handler = RotatingFileHandler('logs/Recipe-site.log', maxBytes=10240,
                                       backupCount=10)
file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)

app.logger.info('Recipe-site startup')


############################# debugging - end ##############################

