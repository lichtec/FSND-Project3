# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session as login_session, redirect, url_for, jsonify

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

#json for jsonify
import json

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.records.record_model import Genre, Artist, Record

# Define the blueprint: 'add', set its url prefix: app.url/
modificationBase = Blueprint('add', __name__, url_prefix='')

'''
    set add methods
'''
@modificationBase.route('/add/record', methods=['GET', 'POST'])
def showRecords():
#    if 'username' not in login_session:
#        return redirect('/login')
    if request.method == 'POST':
        newRecord = Record(
            name=request.form['title'], )
        session.add(newRestaurant)
        flash('New Restaurant %s Successfully Created' % newRestaurant.name)
        session.commit()
        return redirect(url_for('showRestaurants'))
    artists = db.session.query(Artist).all()
    genres = db.session.query(Genre).all()
    if 'username' not in login_session:
        return render_template("records/add_records.html", artists = artists, genres = genres, loggedIn = False)
    else:
        return render_template("records/add_records.html", artists = artists, genres = genres, loggedIn = True)