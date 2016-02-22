# -*- coding: UTF-8 -*-

from flask import render_template, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user

from . import main
from .. import mongo
from .forms import SayingForm
from ..models import Permission
from ..decorators import permission_required


@main.route('/')
def index():
    sayings = list(mongo.db.sayings.find())
    return render_template('index.html', sayings=sayings)


@main.route('/post-saying', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.POST)
def post_saying():
	form = SayingForm()
	if form.validate_on_submit():
		text = form.text.data
		user = current_user.get_id()
		origins = form.origins.data if form.origins.data else []
		tags = form.tags.data if form.tags.data else []
		Saying.add_saying(
			            text=text,
			            added_by=user,
			            origins=origins,
			            tags=tags)
		flash("saying successfully added")
		return redirect(request.args.get('next') or url_for('main.index'))
	return render_template('post_saying.html', form=form)