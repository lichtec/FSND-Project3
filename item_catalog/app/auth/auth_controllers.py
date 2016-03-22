# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangError
import httplib2
import requests

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
from app.records.auth_model import User

CLIENT_ID = json.loads(open('/config/client_secret_821825718249-6am7odj81p1gvdu7q1jfmpsd8v7ugu76.apps.googleusercontent.com.json', 'r').read())['web']['client_id']

# Define the blueprint: 'auth', set its url prefix: app.url/auth
authBase = Blueprint('auth', __name__, url_prefix='')

# Set the route and accepted methods
@authBase.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("auth/login.html")