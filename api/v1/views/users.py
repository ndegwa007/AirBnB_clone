#!/usr/bin/python3
"""users views"""
from api.v1.views.index import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """retrieve all users"""
    users = storage.all(User).values()

    res = [user.to_dict() for user in users]
    return jsonify(res)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """retrieve a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def drop_user(user_id):
    """delete a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """create a new user"""
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'email' not in request.get_json():
        abort(400, "Missing email")
    if 'password' not in request.get_json():
        abort(400, "Missing password")
    data = request.get_json()
    new_user = User(**data)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """update user details"""
    user = storage.get(User, user_id)
    if not request.get_json():
        abort(400, "Not a JSON")

    data = request.get_json()
    ignore = ['id', 'email', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
