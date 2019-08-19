#search views

from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from recipe_app import db, app


from recipe_app.models import User, RecipePost
from recipe_app.search.forms import SearchForm




###########  Blue print ################

search = Blueprint('search', __name__)


###########  Blue end ################




