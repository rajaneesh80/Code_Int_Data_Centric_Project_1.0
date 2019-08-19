#user views
from sqlalchemy.exc import IntegrityError
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from recipe_app import db
from recipe_app import app
from werkzeug.urls import url_parse

#from recipe_app import fhotos
from recipe_app.models import User, RecipePost
from recipe_app.users.forms import RegistrationForm, LoginForm, UpdateUserForm, \
    ResetPasswordRequestForm, ResetPasswordForm

from werkzeug import FileStorage
from werkzeug.utils import secure_filename
from recipe_app.tools import upload_file_to_s3, list_files_in_s3, delete_file_from_s3
from recipe_app.email import send_password_reset_email


users = Blueprint('users', __name__)

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data
                        )

            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('users.login'))

        except IntegrityError:
            db.session.rollback()
            flash(f'either email {form.email.data} or username {form.username.data} already taken : !', 'danger')
            

    return render_template('register.html', form=form)



# login
@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        #if user.check_password(form.password.data) and user is not None:
        if user is not None and user.check_password(form.password.data):

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


            if current_user.picture is not None and current_user.picture != image_url:
                flash("User picture updated")
            current_user.picture = image_url

        else:
            image_url = current_user.picture

        ##############################################################
        try:
            if current_user.username is not None and current_user.username != form.username.data:
                #flash("User name updated")
                current_user.username = form.username.data
            
            ##############################################################
            
            if current_user.email is not None and current_user.email != form.email.data:
                #flash("User email updated")
                current_user.email = form.email.data

            ##############################################################
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            flash(f'either email {form.email.data} or username {form.username.data} already taken : !', 'danger')

        
        return redirect(url_for('users.account'))
        ##############################################################

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', form=form)


# get all the recipe of user

@users.route("/<username>")
def user_recipies(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    recipies_posted = RecipePost.query.filter_by(author=user).order_by(RecipePost.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_recipe_posts.html', recipies_posted=recipies_posted, user=user)

##################### rest password ##############################


@users.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('users.login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)



@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('core.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', form=form)


##################### rest password end ##############################



















