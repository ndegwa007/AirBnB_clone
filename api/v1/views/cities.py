#!/usr/bin/python3
"""views for city objects"""
from api.v1.views.index import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """retrieve all cities in a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    res = [cty.to_dict() for cty in state.cities]
    return jsonify(res)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """retrieve a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """delete a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """post a new city"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    data = request.get_json()
    new_city = City(**data)
    new_city.state_id = state.id
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """update a city"""
    cty = storage.get(City, city_id)
    if not cty:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    data = request.get_json()
    ignore = ['id', 'state_id', 'create_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(cty, key, value)
    storage.save()
    return make_response(jsonify(cty.to_dict()), 200)
