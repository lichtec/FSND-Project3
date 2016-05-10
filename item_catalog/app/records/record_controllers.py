# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session as login_session, redirect, url_for, jsonify

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# json for jsonify
import json

# Import the database object from the main app module
from app import db

# Import module models
from app.records.record_model import Genre, Artist, Record

# Define the blueprint: 'record', set its url prefix: app.url/
recordBase = Blueprint('record', __name__, url_prefix='')

'''
    Set the route and accepted methods RECORDS
'''


@recordBase.route('/', methods=['GET', 'POST'])
@recordBase.route('/records', methods=['GET', 'POST'])
def showRecords():
    # pulling all record information takes some joins
    # using outjoins to handle possible deletes of artists and genres
    records = db.session.query(Record.id, Record.title, Record.year, Record.description, Record.artist_id, Record.record_image, Artist.artist_name,
                               Genre.genre_name).outerjoin(Artist).outerjoin(Genre).all()
    if 'username' not in login_session:
        return render_template("records/records.html", records=records, loggedIn=False)
    else:
        return render_template("records/records.html", records=records, loggedIn=True)


@recordBase.route('/json', methods=['GET'])
@recordBase.route('/records/json', methods=['GET'])
def showRecordsJSON():
    # For JSON endpoint using just record to simplify results
    records = db.session.query(Record).all()
    return jsonify(records=[r.serialize for r in records])


@recordBase.route('/records/<int:record_id>/', methods=['GET', 'POST'])
def showRecordInfo(record_id):
    # pulling individual record info
    record = db.session.query(Record.id, Record.title, Record.year, Record.description, Record.artist_id, Record.record_image,
                              Artist.artist_name, Genre.genre_name).filter_by(id=record_id).outerjoin(Artist).outerjoin(Genre).one()
    if 'username' not in login_session:
        return render_template("records/record_info.html", record=record, loggedIn=False)
    else:
        return render_template("records/record_info.html", record=record, loggedIn=True)


@recordBase.route('/records/<int:record_id>/json', methods=['GET'])
def showRecordsInfoJSON0(record_id):
    record = db.session.query(Record).filter_by(id=record_id).one()
    return jsonify(record=[record.serialize])


'''
    Set the route and accepted methods ARTIST
'''


@recordBase.route('/artists', methods=['GET', 'POST'])
def showArtists():
    artists = db.session.query(Artist).all()
    if 'username' not in login_session:
        return render_template("artists/artists.html", artists=artists, loggedIn=False)
    else:
        return render_template("artists/artists.html", artists=artists, loggedIn=True)


@recordBase.route('/artists/json', methods=['GET'])
def showArtistsJSON():
    artists = db.session.query(Artist).all()
    return jsonify(artists=[r.serialize for r in artists])


@recordBase.route('/artists/<int:artist_id>/', methods=['GET', 'POST'])
def showArtistInfo(artist_id):
    artist = db.session.query(Artist).filter_by(id=artist_id).one()
    records = db.session.query(Record).filter_by(artist_id=artist_id).all()
    if 'username' not in login_session:
        return render_template("artists/artist_info.html", artist=artist, records=records, loggedIn=False)
    else:
        return render_template("artists/artist_info.html", artist=artist, records=records, loggedIn=True)


@recordBase.route('/artists/<int:artist_id>/json', methods=['GET'])
def showArtistInfoJSON(artist_id):
    artist = db.session.query(Artist).filter_by(id=artist_id).one()
    return jsonify(artist=[artist.serialize])

'''
    Set the route and accepted methods GENRE
'''


@recordBase.route('/genres', methods=['GET', 'POST'])
def showGenres():

    genres = db.session.query(Genre).all()
    if 'username' not in login_session:
        return render_template("genres/genres.html", genres=genres, loggedIn=False)
    else:
        return render_template("genres/genres.html", genres=genres, loggedIn=True)


@recordBase.route('/genres/json', methods=['GET'])
def showGenresJSON():
    genres = db.session.query(Genre).all()
    return jsonify(genres=[r.serialize for r in genres])


@recordBase.route('/genres/<int:genre_id>/', methods=['GET', 'POST'])
def showGenreInfo(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).one()
    artists = db.session.query(Artist).filter_by(genre_id=genre_id)
    if 'username' not in login_session:
        return render_template("genres/genre_info.html", genre=genre, artists=artists, loggedIn=False)
    else:
        return render_template("genres/genre_info.html", genre=genre, artists=artists, loggedIn=True)


@recordBase.route('/genres/<int:genre_id>/json', methods=['GET'])
def showGenreInfoJSON(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).one()
    artist = db.session.query(Genre).filter_by(id=genre_id).one()
    return jsonify(genre=[genre.serialize])
