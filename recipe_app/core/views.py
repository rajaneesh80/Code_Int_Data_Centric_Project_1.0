
#Core.Views

from flask import render_template, request, Blueprint
from recipe_app.models import RecipePost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    all_recipies_posts = RecipePost.query.order_by(RecipePost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', all_recipies_posts = all_recipies_posts)

@core.route('/info')
def info():
    return render_template('info.html')
