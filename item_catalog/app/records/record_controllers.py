# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.records.record_forms import LoginForm

# Import module models (i.e. User)
from app.records.record_model import Genre, Artist, Record

# engine = db.create_engine('sqlite:///app.db')
# db.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# Define the blueprint: 'auth', set its url prefix: app.url/auth
recordBase = Blueprint('auth', __name__, url_prefix='')

# Set the route and accepted methods
@recordBase.route('/', methods=['GET', 'POST'])
def showRecords():
    

    records = db.session.query(Record.title, Record.year, Record.description, Artist.artist_name, Genre.genre_name).join(Artist).join(Genre)
    # print records[0].keys()

    return render_template("records/welcome.html", records = records)