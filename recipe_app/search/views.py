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

# @search.route('/search', methods=['GET','POST'])
# def search_result():

# 	form = SearchForm()
# 	#recipe_search = RecipePost.query.all()

# 	if form.validate_on_submit():
# 		recipe_search = RecipePost.filter(RecipePost.recipe_name.like('%' + form.form.data + '%'))

		
# 		return render_template('search.html', form=form, recipe_search = recipe_search )

# 	else:
# 		page = request.args.get('page', 1, type=int)
# 		all_recipies_posts = RecipePost.query.order_by(RecipePost.date.desc()).paginate(page=page, per_page=10)
# 		return render_template('nosearch.html', form=form, all_recipies_posts = all_recipies_posts)



@search.route('/search', methods=['GET','POST'])
def search_result():

	form = SearchForm()
	recipe_search = RecipePost.query.all()

	if form.validate_on_submit():
		#recipe_search = recipe_search.filter(RecipePost.recipe_name.like('%' + form.form.data + '%'))
		#recipe_search = recipe_search.filter_by(RecipePost.recipe_name.like('%' + form.form.data + '%').first())
		#recipe_search = recipe_search.filter_by(RecipePost.recipe_name.first())
		#recipe_search = recipe_search.filter_by(RecipePost.recipe_name.first())
		#recipe_search = RecipePost.filter_by(RecipePost.recipe_name.order_by(RecipePost.date.desc()))

		#recipe_search = RecipePost.filter_by(RecipePost.recipe_name.order_by(RecipePost.date.desc()))

		recipe_search =RecipePost.query.order_by(RecipePost.recipe_name.like('%' + form.form.data + '%'))
		#unique_result = SPInfo.query.filter_by(NRCS_Species=keywords).first() or SPInfo.query.filter_by(NRCS_CommonName=keywords).first()
	#page = request.args.get('page', 1, type=int)
	#recipe_search =recipe_search.order_by(RecipePost.date.desc()).paginate(page=page, per_page=10)
		return render_template('search.html', recipe_search = recipe_search, form=form)
	return render_template('search.html', recipe_search = recipe_search)

	# else:
	# 	page = request.args.get('page', 1, type=int)
	# 	all_recipies_posts = RecipePost.query.order_by(RecipePost.date.desc()).paginate(page=page, per_page=10)
	# 	return render_template('nosearch.html', form=form, all_recipies_posts = all_recipies_posts)


# @search.route('/search', methods=['GET','POST'])
# def search_result():
# 	form = SearchForm()
# 	if form.validate_on_submit():
# 		search_term = form.query.data
# 		recipe_search = RecipePost.query.all()
# 		return render_template('search.html', form=form, recipe_search = recipe_search )
# 	return render_template('search.html', form=form)

	# if form.validate_on_submit():
	# 	recipe_search = recipe_search.filter(RecipePost.recipe_name.like('%' + form.form.data + '%'))

	# page = request.args.get('page', 1, type=int)
	# recipe_search =recipe_search.order_by(RecipePost.date.desc()).paginate(page=page, per_page=10)
	# return render_template('search.html', form=form, recipe_search = recipe_search )