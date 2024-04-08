#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

flk = Flask(__name__)


@flk.route("/", strict_slashes=False)
def display():
    return "Hello HBNB!"


if __name__ == "__main__":
    flk.run(host='0.0.0.0', port=5000)
