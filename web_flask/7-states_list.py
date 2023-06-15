#!/usr/bin/python3
"""run a flask app"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """return the states name and id"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def killsession(*args):
    """close the db session"""
    storage.close()


if __name__ == '__main__':
    """Run app"""
    app.run(host='0.0.0.0', port=5000)
