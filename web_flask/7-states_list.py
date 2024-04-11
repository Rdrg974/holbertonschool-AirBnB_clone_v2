#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask, render_template

flk = Flask(__name__)


@flk.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@flk.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    flk.run(host="0.0.0.0", port=5000)
