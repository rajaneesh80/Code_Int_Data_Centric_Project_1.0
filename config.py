import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
top_level_dir = os.path.abspath(os.curdir)
load_dotenv(os.path.join(basedir, '.env'))



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'add-your-random-key-here'
    S3_BUCKET = os.environ.get('S3_BUCKET')
    S3_KEY = os.environ.get('S3_KEY')
    S3_SECRET = os.environ.get('S3_SECRET_ACCESS_KEY')
    S3_LOCATION = 'http://{}.s3.eu-west-2.amazonaws.com/'.format(S3_BUCKET)
    #ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

 