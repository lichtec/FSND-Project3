# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from app.records.record_model import Base, Genre, Artist, Record
 
engine = create_engine('sqlite:///app.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


#Test Genres
genre1 = Genre(genre_name = "Jazz", description='Jazz is a music genre that originated from African American communities of New Orleans in the United States during the late 19th and early 20th centuries. It emerged in the form of independent traditional and popular musical styles, all linked by the common bonds of African American and European American musical parentage with a performance orientation.', genre_image='http://i.imgur.com/SCZGI6M.jpg')
session.add(genre1)

genre2 = Genre(genre_name = "R&B", description='Rhythm and blues, often abbreviated as R&B or RnB, is a genre of popular African-American music that originated in the 1940s.', genre_image='http://i.imgur.com/2OVemx8.jpg')
session.add(genre2)

genre3 = Genre(genre_name = "Hip-Hop", description='Hip hop music, also called hip-hop or rap music, is a music genre formed in the United States in the 1970s that consists of a stylized rhythmic music that commonly accompanies rapping, a rhythmic and rhyming speech that is chanted', genre_image='http://i.imgur.com/o6U043z.jpg')
session.add(genre3)

genre4 = Genre(genre_name = "Country", description='Country music is a genre of American popular music that originated in the Southern United States in the 1920s. It takes its roots from the southeastern genre of American folk music and Western music.', genre_image='http://i.imgur.com/PgZe1Ym.jpg')
session.add(genre4)

genre5 = Genre(genre_name = "Alt-Rock", description='Alternative rock (also called alternative music, alt-rock or simply alternative) is a genre of rock music that emerged from the independent music underground of the 1980s and became widely popular in the 1990s and 2000s.', genre_image='http://i.imgur.com/8LqARG7.jpg')
session.add(genre5)

genre6 = Genre(genre_name = "Metal", description='Heavy metal (or simply metal) is a genre of rock music[1] that developed in the late 1960s and early 1970s, largely in the United Kingdom and the United States. With roots in blues rock and psychedelic rock,the bands that created heavy metal developed a thick, massive sound, characterized by highly amplified distortion, extended guitar solos, emphatic beats, and overall loudness.', genre_image='http://i.imgur.com/GkVIiRu.jpg')
session.add(genre6)

genre7 = Genre(genre_name = "Reggae", description='Reggae is a music genre that originated in Jamaica in the late 1960s. The term also denotes the modern popular music of Jamaica and its diaspora. While sometimes used in a broad sense to refer to most types of popular Jamaican dance music, the term reggae more properly denotes a particular music style that was strongly influenced by traditional mento as well as American jazz and rhythm and blues, especially the New Orleans R&B practiced by Fats Domino and Allen Toussaint, and evolved out of the earlier genres ska and rocksteady.', genre_image='http://i.imgur.com/jjnn12d.jpg')
session.add(genre7)

genre8 = Genre(genre_name = "Soundtrack", description='A soundtrack, also written sound track, can be recorded music accompanying and synchronized to the images of a motion picture, book, television program or video game; a commercially released soundtrack album of music as featured in the soundtrack of a film or TV show; or the physical area of a film that contains the synchronized recorded sound.', genre_image='http://i.imgur.com/6xQp4dA.jpg')
session.add(genre8)

genre9 = Genre(genre_name = 'JPop', description='''J-pop (often stylized as J-POP; Japanese: jeipoppu; an abbreviation for Japanese pop), natively also known simply as pops, is a musical genre that entered the musical mainstream of Japan in the 1990s. Modern J-pop has its roots in traditional Japanese music, but significantly in 1960s pop and rock music, such as The Beatles and The Beach Boys, which led to Japanese rock bands such as Happy End fusing rock with Japanese music in the early 1970s. J-pop was further defined by new wave groups in the late 1970s, particularly electronic synthpop band Yellow Magic Orchestra and pop rock band Southern All Stars. Eventually, J-pop replaced kayokyoku ("Lyric Singing Music", a term for Japanese pop music from the 1920s to the 1980s) in the Japanese music scene. The term was coined by the Japanese media to distinguish Japanese music from foreign music, and now refers to most Japanese popular music. The musical genre has been immensely influential in many other music styles, and hence those of neighboring regions, where the style has been copied by neighboring Asian regions, who have also borrowed the name to form their own musical identities.''', genre_image='http://i.imgur.com/sKC8WZc.jpg')
session.add(genre9)

genre10 = Genre(genre_name = "Pop", description='Pop music is a genre of popular music that originated in its modern form in the Western world during the 1950s and 1960s, deriving from rock and roll. The terms "popular music" and "pop music" are often used interchangeably, although the former describes all music that is popular (and can include any style).', genre_image='http://i.imgur.com/wOgZP8m.jpg')
session.add(genre10)

session.commit()

artist1 = Artist(artist_name = 'Miles Davis', genre_id=1, artist_image='http://i.imgur.com/EljvyDY.jpg')
session.add(artist1)

artist2 = Artist(artist_name = 'Leon Bridges', genre_id=2, artist_image='http://i.imgur.com/naeXlX1.jpg')
session.add(artist2)

artist3 = Artist(artist_name = 'Nas', genre_id=3, artist_image='http://i.imgur.com/LbrPvjr.jpg')
session.add(artist3)

artist4 = Artist(artist_name = 'Sturgill Simpson', genre_id=4, artist_image='http://i.imgur.com/B9DTjJT.jpg')
session.add(artist4)

artist5 = Artist(artist_name = 'Neutral Milk Hotel', genre_id=5, artist_image='http://i.imgur.com/AU3JtHN.jpg')
session.add(artist5)

artist6 = Artist(artist_name = 'Led Zeppelin', genre_id=6, artist_image='http://i.imgur.com/GbPVHdv.jpg')
session.add(artist6)

artist7 = Artist(artist_name = 'Bob Marley', genre_id=7, artist_image='http://i.imgur.com/OBpbaf4.jpg')
session.add(artist7)

artist8 = Artist(artist_name = 'Tyler Bates', genre_id=8, artist_image='http://i.imgur.com/OxUM6fk.jpg')
session.add(artist8)

artist9 = Artist(artist_name = 'Nujabes', genre_id=9, artist_image='http://i.imgur.com/iI9wNe8.jpg')
session.add(artist9)

artist10 = Artist(artist_name = 'Parquet Courts', genre_id=10, artist_image='http://i.imgur.com/QOlfP08.jpg')
session.add(artist10)


record1 = Record(title='King of Blue', artist_id=1, genre_id=1, year=1959, description='''Regarded by many critics as the greatest jazz album of all time and Davis's masterpiece. This 1959 album's influence on music, including jazz, rock and classical, has led music writers to acknowledge it as one of the most influential albums of all time. This septet features Jazz heavyweights John Coltrane, Bill Evans and Cannonball Adderley. Newly remastered and pressed on 180g vinyl.''', record_image='http://i.imgur.com/vgk5RB4.jpg')
session.add(record1)

record2 = Record(title='Coming Home', artist_id=2, genre_id=2, year=2015, description='''Leon Bridges is the 'out of almost nowhere' story that only comes along once in a while. Awareness of Leon Bidges and his unique craft continues to grow authentically and consistently. 

It was only last summer that Leon was singing open mics in his hometown Fort Worth, TX. One of those open mics was attended by Austin Jenkins and Josh Block of the notable indie band White Denim who were absolutely floored by Leon's voice, songs, and creative vision. 

They soon after set-up shop in a makeshift studio and recorded the album's opener "Coming Home" completely live to tape. This first take is exactly what you hear opening the album. The remaining 9 songs followed in a burst of creativity and inspiration.

Leon was the breakout artist of 2015's SXSW, and performed to capacity crowds at A-level events including Heartbreaker at Willie Nelson's ranch, the Gorilla-vs-Bear HypeHotel showcase, Spotify House and Saint David's Church. His soulful, movement based performances and adept backing band garnered strong reviews from a variety of top-level media including the New York Times, Billboard and Grantland amongst many others.''', record_image='http://i.imgur.com/vnAY2kx.jpg')
session.add(record2)

record3 = Record(title='Illmatic', 
                 artist_id=3, genre_id=3, year=1994, description='''Nasir Jones made this debut album at the age of 20, already armed with the calm perceptiveness and been-there-done-that attitude of a much older ghetto vet, though sometimes his inner callow youth shows itself. Illmatic is a look back at a life spent in the culture of the projects, acknowledging joy as much as pain and taking note of violence as a fact of his environment rather than a focus of his life. It's enlivened by Nas's kicky, deep-threaded multiple rhymes--you can tell he grew up listening to Mr. Magic's rap show and internalizing the secrets of everybody's flow--and by tracks from a bunch of all-stars, including the Large Professor, DJ Premier, and, most memorably, Q-Tip ("One Love")''', record_image='http://i.imgur.com/QwbGCdt.jpg')
session.add(record3)

record4 = Record(title='''A Sailor's Guide To Earth''', artist_id=4, genre_id=4, year=2016, description='''Produced by Simpson, A Sailor's Guide To Earth was written-beginning to end-as a letter to his first child who arrived during the summer of 2014 and features eight original songs as well as a rendition of Nirvana's "In Bloom."
Recorded primarily at Nashville's The Butcher Shoppe, Simpson was joined in the studio by Grammy Award-winning engineer David Ferguson (Johnny Cash, John Prine, "Cowboy" Jack Clement) and assistant engineer Sean Sullivan. Along with members of his touring band, the album features Dave Roe on bass, Dan Dugmore on steel guitar, Dougie Wilkinson on bagpipes, Garo Yellin and Arthur Cook on cello, Jonathan Dinklage and Whitney LaGrange on violin and special guests The Dap-Kings.
A Sailor's Guide To Earth is Simpson's third full-length album and follows his break-through, Grammy-nominated 2014 release, Metamodern Sounds In Country Music. Beloved by critics and fans, the record was featured on year-end "best of" lists at The New York Times, Rolling Stone, the Village Voices' Pazz and Jop, Rolling Stone Country, NPR Music, American Songwriter, Stereogum, the Los Angeles Times, KCRW, Pitchfork, The Washington Post and many others.''', record_image='http://i.imgur.com/Yrmgqjh.jpg')
session.add(record4)

record5 = Record(title='In The Aeroplane Over The Sea', artist_id=5, genre_id=5, year=1998, description='''Named Best Album of the 1990s by Magnet Magazine, Aeroplane gives us Jeff Mangum's powerful solo acoustic work, full horn-section marches, history, religion, & sex -- everything you hoped for and more! Now available on high quality 180 gm vinyl! Includes coupon for MP3 download of the entire album.''', record_image='http://i.imgur.com/BGjOtXW.jpg')
session.add(record5)

record6 = Record(title='Led Zeppelin I', artist_id=6, genre_id=6, year=1969, description='''Led Zeppelin is the eponymous debut studio album by the English rock band Led Zeppelin. It was recorded in October 1968 at Olympic Studios in London and released on Atlantic Records on 12 January 1969 in the United States and 31 March in the United Kingdom. Featuring integral contributions from each of the group's four members, the album established their fusion of blues and rock. It also attracted a large and devoted following to the band; Zeppelin's take on the emerging heavy rock sound endeared them to parts of the counterculture on both sides of the Atlantic.''', record_image='http://i.imgur.com/ETqCdcw.jpg')
session.add(record6)

record7 = Record(title='Legend', artist_id=7, genre_id=7, year=1984, description='''Legend is a compilation album by Bob Marley and the Wailers, released in 1984 by Island Records, catalogue BMW 1 in the United Kingdom and 90169-1 in the United States. It is essentially a greatest hits collection of singles in its original vinyl format, and the best-selling reggae album of all-time, with over 15 million copies sold in the United States and an estimated 25 million copies sold globally.''', record_image='http://i.imgur.com/UPgm7dO.jpg')
session.add(record7)

record8 = Record(title='Guardians of the Galaxy Deluxe Vinyl Edition', artist_id=8, genre_id=8, year=2014, description='''Collector's Edition 2 disc GUARDIANS OF THE GALAXY vinyl includes AWESOME MIX VOL. 1, the collection of songs featured in the film. Music plays a major role in GUARDIANS OF THE GALAXY as the 1970s songs featured in the film are part of the storyline in a unique way. Explaining how the songs come to play in the story, director James Gunn says, 'One of the main story points in the movie is that Quill has this compilation tape (Awesome Mix #1) that he got from his mother before she died that she made for him. It was of songs that she loved, all songs from the 1970s, and that's the only thing he has left of his mother and that's the only thing he has left of his home on Earth. He uses that as a connection to his past and to the sadness that he feels of having left all that and lost all that.' As well as, the complete official original score from the film as composed by Tyler Bates.''', record_image='http://i.imgur.com/1mlLtjM.jpg')
session.add(record8)
record9 = Record(title='Samurai Champloo [Vinyl Double LP] Soundtrack', artist_id=9, genre_id=9, year=2010, description='''Triple vinyl set of hip hop electronica from Fat Jon, Force Of Nature, Nujabes, and Tsutchie from the popular anime series that mixes hip hop culture and music with Japanese samurai culture. Full pic sleeve. Out of print since early 2008 now available again.''', record_image='http://i.imgur.com/B3bVRBG.jpg')
session.add(record9)

record10 = Record(title='Human Performance', artist_id=10, genre_id=10, year=2016, description='THuman Performance is the fifth studio album by American punk rock band Parquet Courts, released on April 8, 2016 on Rough Trade Records', record_image='http://i.imgur.com/jxl5iwE.jpg')
session.add(record10)

session.commit()



print "Added a whole bunch of records and such"