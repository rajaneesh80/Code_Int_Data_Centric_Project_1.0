#Recipe Form 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, configure_uploads, IMAGES


class RecipePostForm(FlaskForm):
   

    ###############################################################
    recipe_image = FileField('Uplod_Recipe_Image', validators=[FileAllowed(IMAGES, 'Images only!')])
    
    ########################################################################

    recipe_name = StringField('Recipe_Name', validators=[DataRequired()])
    #####################################################################
    course = StringField('Course', validators=[DataRequired()])
    food_category = StringField('Food_Category', validators=[DataRequired()])
    cuisine = StringField('Cuisine', validators=[DataRequired()])
    prep_time = StringField('Prep_Time', validators=[DataRequired()])
    cook_time = StringField('Cook_Time', validators=[DataRequired()])
    allergens = StringField('Allergens', validators=[DataRequired()])
    serving = StringField('Serving', validators=[DataRequired()])
    ##########################
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    recipe_description = TextAreaField('Recipe_Description', validators=[DataRequired()])
    submit = SubmitField('Post-Your-Receipe')

#########################################
