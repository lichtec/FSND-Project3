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
    set record methods
'''
@modificationBase.route('/records/add', methods=['GET', 'POST'])
def addRecords():
    if 'username' not in login_session:
        return redirect('/login')
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

@modificationBase.route('/records/<int:record_id>/edit', methods=['GET', 'POST'])
def editRecords(record_id):
#    if 'username' not in login_session:
#        return redirect('/login')
    record = db.session.query(Record.id, Record.title, Record.year, Record.description, Record.artist_id, Artist.artist_name, 
        Genre.genre_name).filter_by(id=record_id).join(Artist).join(Genre).one()
    artists = db.session.query(Artist).all()
    genres = db.session.query(Genre).all()
    if request.method == 'POST':
        editRecord = db.session.query(Record).filter_by(id = record_id).one()
        print editRecord
        if request.form['title']:
            editRecord.title = request.form['title']
        if request.form['artist_Sel']:
            artist_id = db.session.query(Artist.id).filter_by(artist_name = request.form['artist_Sel']).one()
            print int(artist_id[0])
            editRecord.artist_id = int(artist_id[0])
        if request.form['genre_Sel']:
            genre_id = db.session.query(Genre.id).filter_by(genre_name = request.form['genre_Sel']).one()
            editRecord.genre_id = int(genre_id[0])
        if request.form['year']:
            editRecord.year = int(request.form['year'])
        if request.form['description']:
            editRecord.description =  request.form['description']
        db.session.add(editRecord)
        flash('Updated Record Successfully')
        db.session.commit()
        return redirect('/records')

    if 'username' not in login_session:
        return render_template("/records/edit_record.html", artists = artists, genres = genres, record=record, loggedIn = False)
    else:
        return render_template("/records/edit_record.html", artists = artists, genres = genres, record=record, loggedIn = True)
    
@modificationBase.route('/records/<int:record_id>/delete', methods=['GET', 'POST'])
def deleteRecords(record_id):
    if 'username' not in login_session:
        return redirect('/login')
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
    
'''
    set artist methods
'''
@modificationBase.route('/artists/add', methods=['GET', 'POST'])
def addArtist():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        genre_id = db.session.query(Genre.id).filter_by(genre_name = request.form['genre_Sel']).one()
        newArtist = Artist(artist_name=request.form['artist_name'], genre_id=genre_id[0])
        db.session.add(newArtist)
        flash('New Artist Successfully Created')
        db.session.commit()
        return redirect('/artists')
    artists = db.session.query(Artist).all()
    genres = db.session.query(Genre).all()
    if 'username' not in login_session:
        return render_template("artists/add_artists.html", artists = artists, genres = genres, loggedIn = False)
    else:
        return render_template("artists/add_artists.html", artists = artists, genres = genres, loggedIn = True)

@modificationBase.route('/artists/<int:artist_id>/edit', methods=['GET', 'POST'])
def editArtists(artist_id):
#    if 'username' not in login_session:
#        return redirect('/login')
    genres = db.session.query(Genre).all()
    editArtist = db.session.query(Artist).filter_by(id = artist_id).one()
    
    if request.method == 'POST':
        print editArtist
        if request.form['artist_name']:
            editArtist.artist_name = request.form['artist_name']
        if request.form['genre_Sel']:
            genre_id = db.session.query(Genre.id).filter_by(genre_name = request.form['genre_Sel']).one()
            editArtist.genre_id = int(genre_id[0])
        db.session.add(editArtist)
        flash('Updated Artist Successfully')
        db.session.commit()
        return redirect('/artists')
    if 'username' not in login_session:
        return render_template("/artists/edit_artist.html", artist = editArtist, genres = genres, loggedIn = False)
    else:
        return render_template("/artists/edit_artist.html", artist = editArtist, genres = genres, loggedIn = True)
    
@modificationBase.route('/artists/<int:artist_id>/delete', methods=['GET', 'POST'])
def deleteArtist(artist_id):
    if 'username' not in login_session:
        return redirect('/login')
    artistToDelete = db.session.query(Artist).filter_by(id=artist_id).one()
    if request.method == 'POST':
        db.session.delete(artistToDelete)
        flash('Artist Successfully Deleted')
        db.session.commit()
        return redirect('/artists')
    if 'username' not in login_session:
        return render_template("/artists/delete_artist.html", artist=artistToDelete, loggedIn = False)
    else:
        return render_template("/artists/delete_artist.html", artist=artistToDelete, loggedIn = True)
    
'''
    set genre methods
'''
@modificationBase.route('/genres/add', methods=['GET', 'POST'])
def addGenre():
#    if 'username' not in login_session:
#        return redirect('/login')
    if request.method == 'POST':
        newGenre = Genre(genre_name=request.form['genre_name'], description=request.form['genre_description'])
        db.session.add(newGenre)
        flash('New Genre Successfully Created')
        db.session.commit()
        return redirect('/genres')
    if 'username' not in login_session:
        return render_template("genres/add_genres.html", loggedIn = False)
    else:
        return render_template("genres/add_genres.html", loggedIn = True)

@modificationBase.route('/genres/<int:genre_id>/edit', methods=['GET', 'POST'])
def editGenre(genre_id):
#    if 'username' not in login_session:
#        return redirect('/login')
    editGenre = db.session.query(Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        if(request.form['genre_name']):
            editGenre.genre_name = request.form['genre_name']
        if(request.form['genre_description']):
            editGenre.description = request.form['genre_description']
        db.session.add(editGenre)
        flash('Genre Successfully Updated')
        db.session.commit()
        return redirect('/genres')
    if 'username' not in login_session:
        return render_template("genres/edit_genres.html", genre=editGenre, loggedIn = False)
    else:
        return render_template("genres/edit_genres.html", genre=editGenre, loggedIn = True)    
@modificationBase.route('/genres/<int:genre_id>/delete', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    genreToDelete = db.session.query(Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        db.session.delete(genreToDelete)
        flash('Genre Successfully Deleted')
        db.session.commit()
        return redirect('/genres')
    if 'username' not in login_session:
        return render_template("/genres/delete_genres.html", genre=genreToDelete, loggedIn = False)
    else:
        return render_template("/genres/delete_genres.html", genre=genreToDelete, loggedIn = True)