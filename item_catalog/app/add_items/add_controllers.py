# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session as login_session, redirect, url_for, jsonify

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
#from app.records.record_model import Genre, Artist, Record

# Define the blueprint: 'add', set its url prefix: app.url/
addBase = Blueprint('add', __name__, url_prefix='')

'''
    set add methods
'''