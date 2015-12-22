#views.py

from item_catalog import app

@app.route('/')
def index():
    return 'Hello World!'