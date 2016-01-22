from flask import render_template
from . import main
from .. import mongo


@main.route('/')
def index():
    sayings = list(mongo.db.sayings.find())
    print sayings
    return render_template('base.html', sayings=sayings)