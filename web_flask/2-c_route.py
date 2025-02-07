#!/usr/bin/python3
""" start a flask web application"""

from flask import Flask, request

app = Flask(__name__)


# define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


# define the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


# Define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays 'C' followed by the value of <text>."""
    # Replace underscore with spaces in the text variable
    formatted_text = text.replace('_', ' ')
    return "c ()".format(formatted_text)


if __name__ == "__main__":
    # Start the flask development server
    # Listen on all available interfaces
    app.run(host='0.0.0.0', port=5000)
