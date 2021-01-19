#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisFun(text):
    """display “C ” followed by the value of the text"""
    space = text.replace("_", " ")
    return 'C {}'.format(space)

@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def pythonisFun(text="is cool"):
    """display “Python ” followed by the value of the text"""
    space = text.replace("_", " ")
    return 'Python {}'.format(space)

app.run(host='0.0.0.0')
