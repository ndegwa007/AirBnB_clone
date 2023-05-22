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
def c_text(text):
    """ c is _ """
    modified_text = text.replace('_', ' ')
    return "C %s" % modified_text

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text=None):
    """ python text """
    if text is None or text == '':
        text = 'is cool'
    else:
        text = text.replace('_', ' ')

    return "Python %s" % text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
