#!/usr/bin/python3
"""Script that starts a Flask web application."""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

flk = Flask(__name__)


@flk.route("/hbnb_filters", strict_slashes=False)
def display_html():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities)


@flk.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    flk.run(host='0.0.0.0', port=5000)
