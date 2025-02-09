#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page with filters for states and amenities."""
    st = storage.all(State).values()
    amen = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=st, amenities=amen)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
