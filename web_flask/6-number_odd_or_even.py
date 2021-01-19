#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template


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
@app.route('/python/<text>', strict_slashes=False)
def pythonisFun(text="is cool"):
    """display “Python ” followed by the value of the text"""
    space = text.replace("_", " ")
    return 'Python {}'.format(space)


@app.route('/number/<int:n>', strict_slashes=False)
def displayInt(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def displayHTMLn(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
