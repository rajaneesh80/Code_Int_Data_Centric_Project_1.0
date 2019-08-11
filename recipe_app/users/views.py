#user views

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from recipe_app import db
from recipe_app import app
#from recipe_app import fhotos
from recipe_app.models import User, RecipePost
from recipe_app.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from werkzeug import FileStorage
from werkzeug.utils import secure_filename
from recipe_app.tools import upload_file_to_s3, list_files_in_s3, delete_file_from_s3


users = Blueprint('users', __name__)

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data
                    )

        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)



# login
@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('You have been logged in!', 'success')

            next = request.args.get('next')

            if next ==None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
        else:flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html',form=form)


# logout
@users.route("/logout")
def logout():
    logout_user()
    flash('You have been logged Out!', 'success')
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():
        ####################################################################
        if form.picture.has_file():

            #############################
            file            = request.files["picture"]
            output          = upload_file_to_s3(file, app.config["S3_BUCKET"])
            filename        = file.filename
            image_url       = str(output)
            ###########################

            #image_url = fhotos.url(fhotos.save(form.picture.data))
            #current_user.picture = image_url
            if current_user.picture is not None and current_user.picture != image_url:
                flash("User picture updated")
            current_user.picture = image_url
        else:
            image_url = current_user.picture
        ##############################################################
        
        if current_user.username is not None and current_user.username != form.username.data:
            flash("User name updated")
        current_user.username = form.username.data
        
        ##############################################################
        #current_user.email = form.email.data
        if current_user.email is not None and current_user.email != form.email.data:
            flash("User email updated")
        current_user.email = form.email.data

        ##############################################################
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))
        ##############################################################

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', form=form)


# gt all the recipe of user

@users.route("/<username>")
def user_recipies(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    recipies_posted = RecipePost.query.filter_by(author=user).order_by(RecipePost.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_recipe_posts.html', recipies_posted=recipies_posted, user=user)



















