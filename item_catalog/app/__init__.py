# Import flask and template operators
from flask import Flask, render_template
from sqlalchemy import create_engine, text

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
engine = db.create_engine('sqlite:///app.db')
db.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app.db = session

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.records.record_controllers import recordBase as record
from app.auth.auth_controllers import authBase as auth

# Register blueprint(s)
app.register_blueprint(record)
app.register_blueprint(auth)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
#Quick and dirty way to create the view I want. Nothing in the docs about a view via sqlalchemy
# db.engine.execute(text('DROP VIEW IF EXISTS CATALOG;'))
# db.engine.execute(text('CREATE VIEW CATALOG AS SELECT RECORD.TITLE AS TITLE, ARTIST.NAME AS ARTIST, GENRE.NAME AS GENRE, RECORD.YEAR AS YEAR,\
# 					RECORD.DESCRIPTION AS DESCRIPTION FROM RECORD LEFT JOIN ARTIST ON RECORD.ARTIST_ID=ARTIST.ID LEFT JOIN GENRE ON RECORD.GENRE_ID = GENRE.ID'))
