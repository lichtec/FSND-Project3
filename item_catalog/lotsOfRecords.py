#lotsOfRecords.py

'''Simple way to place data in the record catalog db so you can get up and running'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, Genre, Artist, Record
 
engine = create_engine('sqlite:///recordcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

print('Starting with Genres')

#Genres
genre1 = Genre(name = "Jazz", description='A type of music of black American origin characterized by improvisation, syncopation, and usually a regular or forceful rhythm, emerging at the beginning of the 20th century. Brass and woodwind instruments and piano are particularly associated with jazz, although guitar and occasionally violin are also used; styles include Dixieland, swing, bebop, and free jazz.')
session.add(genre1)
session.commit()

genre2 = Genre(name = "R&B", description='A form of popular music of African-American origin that arose during the 1940s from blues, with the addition of driving rhythms taken from jazz. It was an immediate precursor of rock and roll.')
session.add(genre2)
session.commit()

genre3 = Genre(name = "Blues", description='Melancholic music of black American folk origin, typically in a twelve-bar sequence. It developed in the rural southern US toward the end of the 19th century, finding a wider audience in the 1940s as blacks migrated to the cities. This urban blues gave rise to rhythm and blues and rock and roll.')
session.add(genre3)
session.commit()

genre4 = Genre(name = "Soundtrack", description='A recording of the musical accompaniment to a movie.')
session.add(genre4)
session.commit()

genre5 = Genre(name = "Indie Rock", description='Indie rock is a genre of alternative rock that originated in the United Kingdom in the 1980s. Indie rock was extremely diverse, with subgenres that include indie pop, jangle pop, and lo-fi, among others.')
session.add(genre5)
session.commit()

genre6 = Genre(name = "Reggae", description='a style of popular music with a strongly accented subsidiary beat, originating in Jamaica. Reggae evolved in the late 1960s from ska and other local variations on calypso and rhythm and blues, and became widely known in the 1970s through the work of Bob Marley; its lyrics are much influenced by Rastafarian ideas.')
session.add(genre6)
session.commit()

#Artist
print('Starting with artists')

artist1 = Artist(name = "Leon Bridges", genre_id = genre2.id)
session.add(artist1)
session.commit()

artist2 = Artist(name = "Muddy Waters", genre_id = genre3.id)
session.add(artist2)
session.commit()

artist3 = Artist(name = "Robert Johnson", genre_id = genre3.id)
session.add(artist3)
session.commit()

artist4 = Artist(name = "Various Artists", genre_id = genre4.id)
session.add(artist4)
session.commit()

artist5 = Artist(name = "The Mountain Goats", genre_id = genre5.id)
session.add(artist5)
session.commit()

artist6 = Artist(name = "The Postal Service", genre_id = genre5.id)
session.add(artist6)
session.commit()

artist7 = Artist(name = "Neutral Milk Hotel", genre_id = genre5.id)
session.add(artist7)
session.commit()

artist8 = Artist(name = "Bob Marley", genre_id = genre6.id)
session.add(artist8)
session.commit()

artist9 = Artist(name = "Ella Fitzgerald", genre_id = genre1.id)
session.add(artist9)
session.commit()

artist10 = Artist(name = "Louis Armstrong", genre_id = genre1.id)
session.add(artist10)
session.commit()

#Records
print('Starting with records')
record1 = Record(title = "Coming Home", artist_id = artist1.id, genre_id = genre1.id, year = 2015, description = "Coming Home is the debut studio album by American gospel and soul singer Leon Bridges, it was released on June 23, 2015, under Columbia Records. The album was written by Leon Bridges, Austin Michael Jenkins, Joshua Block, Chris Vivion and produced by Niles City Sound.The album was supported by two singles; 'Coming Home' and 'Smooth Sailin'. Upon its release, Coming Home received generally positive reviews from critics. At Metacritic, the album received an average score of 78, based on 21 reviews. The album is nominated for Best R&B Album at the 58th Annual Grammy Awards to be held in February 2016.")
session.add(record1)
session.commit()

record2 = Record(title = "Best of Muddy Waters", artist_id = artist2.id, genre_id = genre3.id, year = 2015, description = "")
session.add(record2)
session.commit()

record3 = Record(title = "The Complete Collection", artist_id = artist4.id, genre_id = genre3.id, year = 2012, description = "A must have for Robert Johnson fans everywhere, this 2LP Gatefold set includes 29 classic songs all written and performed by the legendary bluesman.")
session.add(record3)
session.commit()

record4 = Record(title = "O Brother, Where Art Thou?", artist_id = artist4.id, genre_id = genre4.id, year = 2015, description = "Limited double vinyl LP picture disc pressing. The critical consensus at the end of 2000 was that it had been one of the weakest film years in recent memory. Which may have been true, despite O Brother, Where Art Thou?, the Coen brothers' delightfully warm and weird Depression-era re-telling of Homer's Odyssey. But for music lovers, 2000 was an amazing year at the movies, and it produced several excellent soundtrack compilations including Almost Famous, Dancer in the Dark, Wonder Boys, and High Fidelity. Even with such steep competition, the soundtrack album for O Brother, Where Art Thou? may be the best of the year. in order to capture the sound of Mississippi circa 1932, the Coens commissioned T-Bone Burnett, a masterful producer whose work with artists like Elvis Costello, Sam Phillips, Joseph Arthur, and Counting Crows has earned him a special place in the folk-rock hall of fame, to research and re-create the country, bluegrass, folk, gospel, and blues of the era.")
session.add(record4)
session.commit()

record5 = Record(title = "The Sunset Tree", artist_id = artist5.id, genre_id = genre5.id, year = 2008, description = "The general musical framework within which The Mountain Goats have worked for ten-plus years has been acoustic guitar, bass, and voice. The lyrics are central to the whole enterprise. Many of the songs involve desperate characters who've found themselves in some trouble. The Mountain Goats is a band led by American singer-songwriter John Darnielle. He began recording in 1991, and he has become known for his highly literary lyrics and, until 2002, his lo-fi recording style. The album is summed up in the final two songs: 'Love, Love, Love' and 'Pale Green Things'.")
session.add(record5)
session.commit()

record6 = Record(title = "Give Up", artist_id = artist6.id, genre_id = genre5.id, year = 2004, description = "It's been nearly two years since the monumentally successful 'Give Up' CD came out. Since then, it's scanned over 350,000 and is currently enjoying sales that are consistently better than any other period during its release. Now comes the vinyl edition, containing a bonus six track EP with the b-sides of both commercially available Postal Service CD singles. Also includes covers by The Shins and Iron & Wine as well as the remixes from 'The District Sleeps Alone Tonight' single.")
session.add(record6)
session.commit()

record7 = Record(title = "In The Aeroplane Over The Sea", artist_id = artist7.id, genre_id = genre5.id, year = 2009, description = "Named Best Album of the 1990s by Magnet Magazine, Aeroplane gives us Jeff Mangum's powerful solo acoustic work, full horn-section marches, history, religion, & sex -- everything you hoped for and more! ")
session.add(record7)
session.commit()

record8 = Record(title = "Legend", artist_id = artist8.id, genre_id = genre6.id, year = 2009, description = "")
session.add(record8)
session.commit()

print "Added Genres, Artist, and Records to the DB"