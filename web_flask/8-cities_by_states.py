#!/usr/bin/python3
"""run a flask app"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """displays html of cities in their states"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    cities = sorted(list(storage.all(City).values()),
                    key=lambda city: city.name)

    return render_template(
            '8-cities_by_states.html',
            states=states,
            cities=cities)


@app.teardown_appcontext
def killsession(exception):
    """close the db session"""
    storage.close()


if __name__ == '__main__':
    """Run app"""
    app.run(host='0.0.0.0', port=5000)
