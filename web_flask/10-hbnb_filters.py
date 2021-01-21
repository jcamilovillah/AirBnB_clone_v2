#!/usr/bin/python3
"""Simple application of Flask
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_func(self):
    """Will excecute after each request
    Closes current sqlalchemy session
    """
    storage.close()


@app.route('/hbnb_filters')
def copyHTML():
    """display a HTML page like 6-index.html"""
    state = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=state,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
