#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from models.city import City
from models.state import State
from flask import render_template, Flask

flk = Flask(__name__)


@flk.route("/states", defaults={'id': None}, strict_slashes=False)
@flk.route("/states/<id>", strict_slashes=False)
def states_id(id):
    states = storage.all(State).values()
    for value in states:
        if value.id == id:
            states = value
            return render_template('9-states.html', states=states, id=id)
    if id is None:
        return render_template("9-states.html", states=states, id=id)
    else:
        return render_template("9-states.html")


@flk.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    flk.run(host='0.0.0.0', port=5000)
