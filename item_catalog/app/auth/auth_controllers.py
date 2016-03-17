# Import flask dependencies
from flask import Blueprint, request, render_template, \
flash, g, session, redirect, url_for, session as login_session

import random, string
    

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

#json for jsonify
import json

# Import the database object from the main app module
from app import db

# Import module forms
from app.records.record_forms import LoginForm

# Import module models (i.e. User)
from app.auth.auth_model import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
authBase = Blueprint('auth', __name__, url_prefix='')

 #Set the route and accepted methods
@authBase.route('/login', methods=['GET', 'POST'])
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('auth/login.html', STATE=state)

#@recordBase.route('/JSON', methods=['GET'])
#def showRecordsJSON():
#    records = db.session.query(Record.id, Record.title, Record.year, Record.description, Artist.artist_name, 
#        Genre.genre_name).join(Artist).join(Genre)
#    return jsonify(records=[r.serialize for r in records])
#
#@recordBase.route('/<int:record_id>/', methods=['GET', 'POST'])
#def showRecordInfo(record_id):
#    record = db.session.query(Record.id, Record.title, Record.year, Record.description, Artist.artist_name, 
#        Genre.genre_name).filter_by(id=record_id).join(Artist).join(Genre).one()
#    print record
#
#    return render_template("records/record_info.html", record = record)
#
#@recordBase.route('/<int:record_id>/JSON', methods=['GET'])
#def showRecordsJSON():
#    record = db.session.query(Record.id, Record.title, Record.year, Record.description, Artist.artist_name, 
#        Genre.genre_name).filter_by(id=record_id).join(Artist).join(Genre).one()
#    return jsonify(record=[r.serialize for r in record])