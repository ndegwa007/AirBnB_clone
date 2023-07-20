#!/usr/bin/python3
"""main flask app run"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')


@app.teardown_appcontext
def session_close(exception):
    """close session"""
    return storage.close()


@app.errorhandler(404)
def error_handler(error):
    """error response"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    if not host or not port:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    else:
        app.run(host=host, port=int(port), threaded=True)
