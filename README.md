# FSND-Project 3

##Description:
Udacity Full Stack Nanodegree Project 3. Creating an item catalog that includes CRUD capabilities and authentication and authorization. Application is based on providing a vinyl record catalog that breaks down into Genres, Artists, and Records.

##Requirements:

* You will need to have the following installed at the version listed as a minimum:

    * Python 2.7
    * Flask==0.10.1
    * Flask-SQLAlchemy==2.1
    * Flask-WTF==0.12
    * httplib2==0.9.2
    * Jinja2==2.8
    * MarkupSafe==0.23
    * oauth2==1.9.0.post1
    * oauth2client==2.0.1
    * requests==2.9.1
    * SQLAlchemy==1.0.12
    * Werkzeug==0.11.5
    * WTForms==2.1
    
*In the same directory as the readme, there is a requirements.txt file. You can use the following command (ran in the directory the file is) to install all of these using pip. The first is for a unix environment the second is for a windows environment.

    >sudo pip install -r requirements.txt
    >pip install -r requirements.txt

##Build Dependencies:

* This code requires Python 2.7. To run the application you'll need the structure unchanged. 

##To Run:

1. To run the application simply use the current structure with all of the files. Basically, don't change anything.

2.  If you would like test data frun the following in the item_catalog directory.

    >python lotsOfRecords.py

3. The first step is to run the following command under the item_catalog directory. It starts up the application and creates the empty db. Once this starts it will run on 0.0.0.0:5000 and is ready for use.

    >python run.py

4. To stop the application hit CTRL-C.

##Open Source Info
* This application is using David Miller's template for Bootstrap. Please see the included folder for more information.
