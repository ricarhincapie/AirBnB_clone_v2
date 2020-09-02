#!/usr/bin/python3
"""Module to start a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start_app():
    """Routes the / GET request
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Routes the /hbnb GET request
    """
    return 'hbnb'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
