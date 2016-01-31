from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user

from . import auth
from .forms import LoginForm, RegistrationForm
from ..email import send_email
from .. import mongo, login_manager
from ..models import User


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed() \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed():
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


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
        token = User.generate_confirmation_token(register_form.username.data)
        send_email(register_form.email.data, 'Confirm Your Account',
                   'auth/email/confirm', username=register_form.username.data,
                   token=token)
        flash('A confirmation email has been sent to you by email', category='alert-info')
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


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!', category='alert-success')
    else:
        flash('The confirmation link is invalid or has expired.', category='alert-danger')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    print 'email is ' + current_user.email
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.', category='alert-info')
    return redirect(url_for('main.index'))
