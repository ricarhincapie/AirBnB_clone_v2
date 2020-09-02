#!/usr/bin/env python3
"""Module to start a Flask web application
"""

from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def start_app():
    """Routes the / GET request
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Routes the /hbnb GET request
    """
    return 'hbnb'


@app.route('/c/<adjective>')
def c_is_fun(adjective):
    """Uses variable rules to modify return according to URL
    """
    return 'C %s' % escape(adjective.replace("_", " "))


# Strict slashes allows that '/python' and '/python/'
# have the same result
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_cool(text='is cool'):
    """Uses variable rules to modify return according to URL
    """
    return 'Python %s' % escape(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
