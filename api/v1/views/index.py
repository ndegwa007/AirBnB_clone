#!/usr/bin/python3
"""index app file"""

from flask import Blueprint, jsonify
from models import storage

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/status')
def status_check():
    """status checker"""
    return {"status": "OK"}


@app_views.route('/stats')
def stats():
    """count checker"""
    res = {}
    cls = ['State', 'City', 'Place', 'Amenity', 'Review', 'User']
    names = ['states', 'cities', 'places', 'amenities', 'reviews', 'users']

    for i in range(len(cls)):
        res[names[i]] = storage.count(cls[i])

    return jsonify(res)
