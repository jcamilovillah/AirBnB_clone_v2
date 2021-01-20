#!/usr/bin/python3
"""Simple application of Flask
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_func(self):
    """Will excecute after each request
    Closes current sqlalchemy session
    """
    storage.close()


@app.route('/states')
def states():
    """Returns Hello HBNB
    """
    data = storage.all(State)
    return render_template('9-states.html', states=data, mode="none")


@app.route('/states/<id>')
def states_id(id):
    """Returns Hello HBNB
    """
    data = storage.all(State)
    for state in data.values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode="id")
    else:
        return render_template('9-states.html', states=data, mode="not")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
