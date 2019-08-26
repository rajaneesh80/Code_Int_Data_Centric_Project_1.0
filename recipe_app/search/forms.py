#Search  form
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from recipe_app.models import RecipePost, User


################## ############################# #################################

#### Search Form start ###############################################

class SearchForm(FlaskForm):
	searchRecipe = StringField('Search', validators=[DataRequired()])


#### Search Form end  ##############################################