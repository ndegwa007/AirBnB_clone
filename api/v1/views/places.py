#!/usr/bin/python3
"""places routes"""
from api.v1.views.index import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.place import Place
from models.city import City


@app_views.route('cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """retrieve all places in a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    res = [place.to_dict() for place in city.places]
    return jsonify(res)


@app_views.route('/places/<place_id>')
def get_place(place_id):
    """retrieve a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())



