from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

from . import auth
from .forms import LoginForm
from .. import mongo, login_manager
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_doc = mongo.db.users.find_one({'_id': form.username.data})
        if user_doc and \
           User.validate_login(user_doc['password_hash'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.', category='alert-danger')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
