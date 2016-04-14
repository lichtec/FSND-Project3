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
    print request.method
    if request.method == 'POST':
        print 'entering post'
        artist_id = db.session.query(Artist.id).filter_by(artist_name = request.form['artist_Sel']).one()
        print artist_id[0]
        genre_id = db.session.query(Genre.id).filter_by(genre_name = request.form['genre_Sel']).one()
        print genre_id
        newRecord = Record(
            title=request.form['title'], artist_id=int(artist_id[0]), genre_id=genre_id[0], year=int(request.form['year']), description=request.form['description'])
        db.session.add(newRecord)
        flash('New Record Successfully Created')
        db.session.commit()
        return redirect('/records')
    artists = db.session.query(Artist).all()
    genres = db.session.query(Genre).all()
    if 'username' not in login_session:
        return render_template("records/add_records.html", artists = artists, genres = genres, loggedIn = False)
    else:
        return render_template("records/add_records.html", artists = artists, genres = genres, loggedIn = True)