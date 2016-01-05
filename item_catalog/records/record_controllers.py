#record_controllers.py

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db

from app.records.record_forms import Welcome

from app.records.record_model import Genre, Artist, Record

mod_record = Blueprint('record', __name__, url_prefix='/') 

@mod_record.route('/', methods=['GET'])
def LandingPage():
	form = Welcome(request.form)

	return render_template(records/welcome.html, form=form)

