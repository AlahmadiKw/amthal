from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError

from .. import mongo
from ..models import User