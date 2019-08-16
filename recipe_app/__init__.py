#main __init__
import os
#import boto3
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
#from flask_uploads import UploadSet, configure_uploads, IMAGES

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

# photos = UploadSet('photos', IMAGES)
# fhotos = UploadSet('fhotos', IMAGES)

# set SECRET_KEY=mysecret

#app.config['SECRET_KEY'] = 'mysecret'

### DATABASE SETUPS ############

basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

###### image ##############################

# app.config['UPLOADED_FHOTOS_DEST'] = 'C:/Code_Int_Data_Centric_Project/recipe_app/static/profile_pics'
# app.config['UPLOADED_PHOTOS_DEST'] = 'C:/Code_Int_Data_Centric_Project/recipe_app/static/recipe_images'

############### image end #################

# configure_uploads(app, photos)
# configure_uploads(app, fhotos)

######### db ###################

db = SQLAlchemy(app)
Migrate(app,db)

#### LOGIN CONFIGS #######

login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"

#### email support #######
mail = Mail(app)

#### BLUEPRINT CONFIGS #######
 
from recipe_app.core.views import core
from recipe_app.error_pages.handlers import error_pages
from recipe_app.users.views import users
from recipe_app.recipe_posts.views import recipe_posts


# Register the apps
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(recipe_posts)

############################# debugging ##############################

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

