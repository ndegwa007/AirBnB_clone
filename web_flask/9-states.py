#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def filter_state_by_id(id=""):
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state = ""
    found = 0
    cities = []

    for i in states:
        if id == i.id:
            state = i
            found = 1
            break

    if found:
        states = sorted(
                state.cities,
                key=lambda k: k.name)
        state = state.name

    if id and not found:
        found = 2

    return render_template(
            '9-states.html',
            state=state,
            array=states,
            found=found)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    """app run"""
    app.run('0.0.0.0', port=5000)
