# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

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
from app.records.record_model import Genre, Artist, Record

# Define the blueprint: 'record', set its url prefix: app.url/
recordBase = Blueprint('record', __name__, url_prefix='')

'''
    Set the route and accepted methods Records
''' 
@recordBase.route('/', methods=['GET', 'POST'])
@recordBase.route('/records', methods=['GET', 'POST'])
def showRecords():
    
    records = db.session.query(Record.id, Record.title, Record.year, Record.description, Artist.artist_name, 
        Genre.genre_name).join(Artist).join(Genre).all()
    print type(records)

    return render_template("records/records.html", records = records)

@recordBase.route('/json', methods=['GET'])
@recordBase.route('/records/json', methods=['GET'])
def showRecordsJSON():
    #records = db.session.query(Record.id, Record.title, Record.year, Record.description, Artist.artist_name, 
       # Genre.genre_name).join(Artist).join(Genre).all()
    records = db.session.query(Record).all()
    print records
    
    return jsonify(records=[r.serialize for r in records])

@recordBase.route('/records/<int:record_id>/', methods=['GET', 'POST'])
def showRecordInfo(record_id):
    record = db.session.query(Record.id, Record.title, Record.year, Record.description, Artist.artist_name, 
        Genre.genre_name).filter_by(id=record_id).join(Artist).join(Genre).one()
    print type(record)

    return render_template("records/record_info.html", record = record)

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
    return render_template("artists/artists.html", artists = artists)

@recordBase.route('/artists/json', methods=['GET'])
def showArtistsJSON():
    artists = db.session.query(Record).all()
    return jsonify(records=[r.serialize for r in artists])

@recordBase.route('/artists/<int:artist_id>/', methods=['GET', 'POST'])
def showArtistInfo(artist_id):
    artist = db.session.query(Artist).filter_by(id=artist_id).one()
    records = db.session.query(Record).filter_by(artist_id=artist_id).all()

    return render_template("artists/artist_info.html", artist = artist, records = records)

@recordBase.route('/artists/<int:artist_id>/json', methods=['GET'])
def showArtistInfoJSON(record_id):
    artist = db.session.query(Artist).filter_by(id=artist_id).one()
    return jsonify(artist=[artist.serialize])