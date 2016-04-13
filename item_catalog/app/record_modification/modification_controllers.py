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
        print 'test'
        artist_id = db.session.query(Artist).filter_by(artist_name = request.form['artist_Sel']).one()
        print artist_id
        genre_id = db.session.query(Genre).filter_by(genre_name = request.form['genre_Sel'])
        print genre_id
        newRecord = Record(
            title=request.form['title'], artist_id=artist_id, genre_id=genre_id, year=request.form['year'], description=request.form['description'])
        session.add(newRestaurant)
        flash('New Restaurant %s Successfully Created' % newRestaurant.name)
        session.commit()
        return redirect(url_for('showRestaurants'))
    artists = db.session.query(Artist).all()
    genres = db.session.query(Genre).all()
    if 'username' not in login_session:
        print request.method
        return render_template("records/add_records.html", artists = artists, genres = genres, loggedIn = False)
    else:
        print request.method
        return render_template("records/add_records.html", artists = artists, genres = genres, loggedIn = True)