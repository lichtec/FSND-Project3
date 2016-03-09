from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from app import db

class Base(db.Model):

	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Base = declarative_base()

class Genre(Base):
	__tablename__ = 'genre'
	
	id = db.Column(db.Integer, primary_key=True)
	genre_name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String, nullable=True)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
					'id': self.id,
					'title': self.title,
					'description' : self.description,
                    'artist_id' :   self.artist_id
        }

    # New instance instantiation procedure
	def __init__(self, name, description):
		self.name = name
		self.description = description
	def __repr__(self):
		return '<Genre %r>' % (self.name)

class Artist(Base):
	__tablename__ = 'artist'
	
	id = db.Column(db.Integer, primary_key=True)
	artist_name = db.Column(db.String(250), nullable=False)
	genre_id = db.Column(db.Integer, ForeignKey('genre.id'))
	genre = db.relationship(Genre)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
					'name': self.artist_name,
					'id': self.id,
                    'genre_id'  : self.genre_id
        }     

    # New instance instantiation procedure
	def __init__(self, name, genre_id):
		self.name     = name
		self.genre_id = genre_id

	def __repr__(self):
		return '<Artist %r>' % (self.artist_name)   

class Record(Base):
	__tablename__ = 'record'
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250), nullable=False)
	artist_id = db.Column(db.Integer, ForeignKey('artist.id'))
	artist = db.relationship(Artist)
	genre_id = db.Column(db.Integer, ForeignKey('genre.id'))
	genre = db.relationship(Genre)
	year = db.Column(db.String, nullable=False) #Not sure about this datatype
	description = db.Column(db.String, nullable=True)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
    				'id': self.id,
    				'title': self.title,
    				'year' : self.year,
    				'description' : self.description,
                    'artist_id' :   self.artist_id,
                    'genre_id'  : self.genre_id
                }
    # New instance instantiation procedure
	def __init__(self, title, artist_id, genre_id, year, description):
		self.title     = title
		self.artist_id = artist_id
		self.genre_id = genre_id
		self.year = year
		self.description = description

	def __repr__(self):
		return '<Record %r>' % (self.title)
	

# engine = create_engine('sqlite:///app/app.db')


# Base.metadata.create_all(engine)