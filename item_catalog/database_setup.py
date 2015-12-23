#database_setup.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Record(Base):
	__tablename__ = 'record'
	
	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	artist_id = Column(Integer, ForeignKey('artist.id')
	artist = relationship(Artist)
	genre_id = Column(Integer, ForeignKey('genre.id')
	genre = relationship(Genre)
	year = Column(Text, nullable=False) #Not sure about this datatype
	description = Column(Text, nullable=True)
	
	@property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
			'title': self.title,
			'year' : self.year,
			'description' : self.description
        }
	
class Artist(Base):
	__tablename__ = 'artist'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	genre_id = Column(Integer, ForeignKey('genre.id')
	genre = relationship(Genre)
	
	@property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }
		
class Genre(Base):
	__tablename__ = 'genre'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	description = Column(Text, nullable=True)
	
	@property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
			'title': self.title,
			'description' : self.description
        }
	
	

