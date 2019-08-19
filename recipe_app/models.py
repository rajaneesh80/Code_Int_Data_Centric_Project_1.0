 #model.py
from recipe_app import app, db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
from hashlib import md5
import jwt

# The user_loader decorator allows flask-login to load the current user
# and grab their id.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


############################# USER MODEL  ##############################

class User(db.Model, UserMixin):

     # Create a table in the db
     __tablename__ = 'users'

     id = db.Column(db.Integer, primary_key = True)
     picture = db.Column(db.String(128), default='default_profile.png', nullable=False)
     email = db.Column(db.String(64), unique=True, index=True)
     username = db.Column(db.String(64), unique=True, index=True)
     password_hash = db.Column(db.String(128))

     # This connects RecipePost to a User Author.

     recipe = db.relationship('RecipePost', backref='author', lazy=True)

     def __init__(self, email, username, password):
         self.email = email
         self.username = username
         self.password_hash = generate_password_hash(password)

     def check_password(self,password):
        return check_password_hash(self.password_hash,password)

     def set_password(self, password):
        self.password_hash = generate_password_hash(password)

     def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

     @staticmethod
     def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


     def __repr__(self):
        return f"UserName: {self.username}"

############################ USER MODEL END #########################################


############################ ADD A RECIPE MODEL  #########################################
class RecipePost(db.Model):
    # Search
    __searchable__ = ['recipe_name']
    # Setup the relationship to the User table
    users = db.relationship(User)
    # Model for the Recipe Posts on Website
    id = db.Column(db.Integer, primary_key=True)
    # we connect the Recipe Posts to a particular author
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ##############################################################################
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ########################################################################
    recipe_image = db.Column(db.String(128), default=None, nullable=True)
    ########################################################################
    recipe_name = db.Column(db.String(164), nullable=False)
    ########################################################################

    course = db.Column(db.String(164), nullable=False)
    food_category = db.Column(db.String(164), nullable=False)
    cuisine = db.Column(db.String(164), nullable=False)
    prep_time = db.Column(db.String(164), nullable=False)
    cook_time = db.Column(db.String(164), nullable=False)
    allergens = db.Column(db.String(164), nullable=False)
    serving = db.Column(db.String(164), nullable=False)

    #############################################################################
    ingredients = db.Column(db.Text, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    

    def __init__(self, recipe_image, recipe_name, ingredients, recipe_description, user_id,
                 course,food_category,cuisine,prep_time,cook_time,allergens,serving):
    
        self.recipe_image = recipe_image
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.recipe_description = recipe_description
        self.user_id =user_id
        ##########################
        self.course = course
        self.food_category = food_category
        self.cuisine = cuisine
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.allergens = allergens
        self.serving = serving

    def __repr__(self):
         return f"Recipe Id: {self.id} --- Date: {self.date} --- Title: {self.recipe_name}"

############################ ADD A RECIPE MODEL  END #########################################
################################################################################################

