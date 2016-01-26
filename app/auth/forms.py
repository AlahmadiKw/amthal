from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from werkzeug.security import generate_password_hash, check_password_hash

from .. import mongo
from ..models import User

# def EmailAlreadyExist(form, field):
#     if mongo.db.users.find({'email': field.data}):
#         raise ValidationError('Email is already used by another user')

class LoginForm(Form):
    regex = '^[A-Za-z][A-Za-z0-9_.]*$'
    username = StringField('username',
                  validators=[
        Required(), Length(8,20), Regexp(regex,0,'Usernames must have only letters, '
                                                 'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Log In')


