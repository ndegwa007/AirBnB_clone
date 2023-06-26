#!/usr/bin/python3
"""start a flask app"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """loads the states and amenities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    return render_template('10-hbnb_filters.html',
                           states=st_ct,
                           amenities=amenities)


@app.teardown_appcontext
def sql_kill(error):
    """kill current sql session"""
    storage.close()


if __name__ == '__main__':
    """run flask app"""
    app.run(host='0.0.0.0', port=5000)
