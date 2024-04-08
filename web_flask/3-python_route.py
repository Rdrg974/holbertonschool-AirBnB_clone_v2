#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

flk = Flask(__name__)


@flk.route("/", strict_slashes=False)
def display_slash():
    return "Hello HBNB!"


@flk.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return "HBNB"


@flk.route("/c/<text>", strict_slashes=False)
def display(text):
    text = text.replace('_', ' ')
    return "C " + text


@flk.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@flk.route('/python/<text>', strict_slashes=False)
def display_py(text):
    text = text.replace('_', ' ')
    return "Python " + text


if __name__ == "__main__":
    flk.run(host='0.0.0.0', port=5000)
