#!/usr/bin/python3
"""places routes"""
from api.v1.views.index import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route('cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
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


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def drop_place(place_id):
    """delete a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """create a new place"""
    city = storage.get(City, city_id)

    if not city:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    data = request.get_json()

    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)

    data['city_id'] = city_id
    new_place = Place(**data)
    new_place.save()
    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """update a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")

    data = request.get_json()
    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_id']
    for key, value in data.items():
        if key not in ignore:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)
