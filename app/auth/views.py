from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import mongo, login_manager
from ..models import User


@auth.route('/login', methods=['POST'])
def login():
    login_form = LoginForm(prefix='login')
    if login_form.validate_on_submit():
        print 'should not be printed'
        user_doc = User.get_user(login_form.username.data)
        if user_doc and \
           User.validate_login(user_doc['password_hash'], login_form.password.data):
            user_obj = User(user_doc['_id'])
            login_user(user_obj)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.', category='alert-danger')
    return render_template('auth/authentication.html',
                           login_form=login_form,
                           register_form=RegistrationForm(prefix='register'))


@auth.route('/register', methods=['POST'])
def register():
    register_form = RegistrationForm(prefix='register')
    if register_form.validate_on_submit():
        User.add_user(email=register_form.email.data,
                      username=register_form.username.data,
                      password=register_form.password.data)
        flash('You can now login.', category='alert-info')
    return render_template('auth/authentication.html',
                           login_form=LoginForm(prefix='login'),
                           register_form=register_form)


@auth.route('/authentication')
def authentication():
    return render_template('auth/authentication.html',
                           login_form=LoginForm(prefix='login'),
                           register_form=RegistrationForm(prefix='register'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='alert-info')
    return redirect(url_for('main.index'))
