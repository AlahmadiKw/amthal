from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from .. import mongo
from ..models import Saying


class SayingForm(Form):

    text = StringField('Saying', validators=[Length(20, 140)])
    # origins = SelectMultipleField('Origins', choices=Saying.get_country_names('english'))
    origins = SelectMultipleField('Origins', choices=Saying.get_tags())
    tags = SelectMultipleField('Tags', choices=Saying.get_tags())
    submit = SubmitField('Post Saying')
