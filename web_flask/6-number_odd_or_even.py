#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template

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


@flk.route("/number/<int:n>", strict_slashes=False)
def display_nbr(n):
    return '' + n


@flk.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    return render_template('5-number.html', n=n)


@flk.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    flk.run(host='0.0.0.0', port=5000)
