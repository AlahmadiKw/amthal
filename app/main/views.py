from flask import render_template, flash
from . import main
from .. import mongo


@main.route('/')
def index():
    sayings = list(mongo.db.sayings.find())
    return render_template('index.html', sayings=sayings)