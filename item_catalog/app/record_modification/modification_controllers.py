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
def addRecords():
#    if 'username' not in login_session:
#        return redirect('/login')
    if request.method == 'POST':
        artist_id = db.session.query(Artist.id).filter_by(artist_name = request.form['artist_Sel']).one()
        genre_id = db.session.query(Genre.id).filter_by(genre_name = request.form['genre_Sel']).one()
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
    
@modificationBase.route('/records/<int:record_id>/delete/', methods=['GET', 'POST'])
def deleteRecords(record_id):
#    if 'username' not in login_session:
#        return redirect('/login')
    recordToDelete = db.session.query(Record).filter_by(id=record_id).one()
    if request.method == 'POST':
        db.session.delete(recordToDelete)
        flash('Record Successfully Deleted')
        db.session.commit()
        return redirect('/records')
    if 'username' not in login_session:
        return render_template("records/delete_record.html", record=recordToDelete, loggedIn = False)
    else:
        return render_template("records/delete_record.html", record=recordToDelete, loggedIn = True)