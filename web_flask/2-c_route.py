#!/usr/bin/python3
#a minimal flask app
from flask import Flask 
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ display hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ c is _ """
    modified_text = text.replace('_', ' ')
    return "C %s" % modified_text


 if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
