#Views Blog_Post
import os
from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user, login_required
from recipe_app import db
from recipe_app import app
#from recipe_app import photos
from recipe_app.models import RecipePost
from recipe_app.recipe_posts.forms import RecipePostForm
from werkzeug import FileStorage
from werkzeug.utils import secure_filename
from recipe_app.tools import upload_file_to_s3, list_files_in_s3, delete_file_from_s3

recipe_posts = Blueprint('recipe_posts',__name__)

@recipe_posts.route('/create',methods=['GET','POST'])
@login_required
def create_recipe():
    form = RecipePostForm()

    if form.validate_on_submit():

        #########################

        file            = request.files["recipe_image"]
        output          = upload_file_to_s3(file, app.config["S3_BUCKET"])
        filename        = file.filename
        image_url       = str(output)

        ##################################




        #########################
        #filename = photos.save(request.files['recipe_image'])
        #image_url = photos.url(photos.save(form.recipe_image.data))
        #image_url = photos.url('https://s3.console.aws.amazon.com/s3/buckets/rajecom/recipe_images')
        ############################
        recipe_post = RecipePost(recipe_image = image_url,
                             ########################
                             recipe_name=form.recipe_name.data,
                             course=form.course.data,
                             food_category=form.food_category.data,
                             cuisine=form.cuisine.data,
                             prep_time=form.prep_time.data,
                             cook_time=form.cook_time.data,
                             allergens=form.allergens.data,
                             serving=form.serving.data,
                             ##########################
                             ingredients=form.ingredients.data,
                             recipe_description=form.recipe_description.data,
                             user_id=current_user.id
                             )
        db.session.add(recipe_post)
        db.session.commit()
        flash("Recipe Post Created")
        return redirect(url_for('core.index'))

    return render_template('create_recipe.html',form=form)


# int: makes sure that the recipe_post_id gets passed as in integer
# instead of a string so we can look it up later.

#read or view the Single Recipe Details
@recipe_posts.route('/<int:recipe_post_id>')
def recipe_post(recipe_post_id):
    # grab the requested recipe post by id number or return 404
    recipe_post = RecipePost.query.get_or_404(recipe_post_id)
    return render_template('recipe_post.html', recipe_name=recipe_post.recipe_name,
                            date=recipe_post.date, recipe=recipe_post
    )

#Update the recipe
@recipe_posts.route("/<int:recipe_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(recipe_post_id):
    recipe_post = RecipePost.query.get_or_404(recipe_post_id)
    if recipe_post.author != current_user:
        # Forbidden, No Access
        abort(403)

    form = RecipePostForm()

    if form.validate_on_submit():
        if form.recipe_image.has_file():

            #############################
            file            = request.files["recipe_image"]
            output          = upload_file_to_s3(file, app.config["S3_BUCKET"])
            filename        = file.filename
            image_url       = str(output)
            ###########################
            
            #image_url = photos.url(photos.save(form.recipe_image.data))
            recipe_post.recipe_image = image_url
        else:
            image_url = recipe_post.recipe_image

        ##################################################################################################################
        recipe_post.recipe_name = form.recipe_name.data
        #######################################
        recipe_post.course=form.course.data
        recipe_post.food_category=form.food_category.data
        recipe_post.cuisine=form.cuisine.data
        recipe_post.prep_time=form.prep_time.data
        recipe_post.cook_time=form.cook_time.data
        recipe_post.allergens=form.allergens.data
        recipe_post.serving=form.serving.data

        #######################################

        recipe_post.ingredients = form.ingredients.data
        recipe_post.recipe_description = form.recipe_description.data

        db.session.commit()
        flash('Recipe Updated')
        return redirect(url_for('recipe_posts.recipe_post', recipe_post_id=recipe_post.id))

    # Pass back the old recipe post information so they can start again with
    # the old text and title.

    elif request.method == 'GET':

        ########################################
        form.recipe_name.data = recipe_post.recipe_name
        ########################################
        form.course.data = recipe_post.course
        form.food_category.data = recipe_post.food_category
        form.cuisine.data = recipe_post.cuisine
        form.prep_time.data = recipe_post.prep_time
        form.cook_time.data = recipe_post.cook_time
        form.allergens.data = recipe_post.allergens
        form.serving.data =recipe_post.serving
        ################################################
        form.ingredients.data = recipe_post.ingredients
        form.recipe_description.data = recipe_post.recipe_description
    return render_template('create_recipe.html', title='Update',
                           form=form)

#Delete the recipe
@recipe_posts.route("/<int:recipe_post_id>/delete", methods=['POST'])
@login_required
def delete_recipe(recipe_post_id):
    recipe_post = RecipePost.query.get_or_404(recipe_post_id)
    if recipe_post.author != current_user:
        abort(403)
    db.session.delete(recipe_post)
    db.session.commit()
    flash('Recipe has been deleted')
    return redirect(url_for('core.index'))
