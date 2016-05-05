# FSND-Project 3

##Description:
Udacity Full Stack Nanodegree Project 3. Creating an item catalog that includes CRUD capabilities and authentication and authorization. Application is based on providing a vinyl record catalog that breaks down into Genres, Artists, and Records.

##Requirements:

* It should be noted to actually use this, you will need to have the following things installed:

    * Python 2.7
    

##Build Dependencies:

* This code requires python 2.7. To run the application you'll need to have tournament.py and you'll need to run tournament.sql to create the tables and the DB. 

##To Run:

1. To run the application you'll need to move tournament.py and tournament.sql to same folder and start-up psql.

2. When psql is running, run the following command `\i tournament.sql` to create the database and all the necessary tables and views and insert the default tournament.

3. You can now run the tournament python methods as necessary. 

##A Note Regarding Multiple Tournaments
Using multiple tournaments is possible but you can choose not to use it. If you don't specify a tournament then the functions wil reference the default tournament. To add an additional tournament use the NewTournament() function.