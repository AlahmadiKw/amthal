from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError

from .. import mongo
from ..models import User

class LoginForm(Form):
    regex = '^[A-Za-z][A-Za-z0-9_.]*$'
    username = StringField('username',
                  validators=[
        Required(), Length(8,20), Regexp(regex,0,'Usernames must have only letters, '
                                                 'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('Username', validators=[
        Required(), Length(8,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords do not match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.email_exists(email=field.data):
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.get_user(username=field.data):
            raise ValidationError('Username already in use.')

