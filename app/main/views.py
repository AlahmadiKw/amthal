from flask import render_template, flash
from . import main
from .. import mongo


@main.route('/')
def index():
    sayings = list(mongo.db.sayings.find())
    print mongo.db.sayings.find_one()
    return render_template('index.html', sayings=sayings)