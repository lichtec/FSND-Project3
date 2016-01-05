#__init__.py

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)

db = SQLAlchemy(app)

from app.record.record_controllers import mod_record as record_module

app.register_blueprint(record_module)

db.create_all()