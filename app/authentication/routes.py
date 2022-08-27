from forms import UserLoginForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            # create User using class made from models.py
            user = User(email, password = password)

            # add new User to database
            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'User-created') # 'User-created' is used to talk to application
            return redirect(url_for('site.home')) # send user back to home page
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('sign_up.html', form=form)


