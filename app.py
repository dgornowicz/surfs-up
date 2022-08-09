# dependency
from flask import flask

# create new flask instance
app = Flask(__name__)

# define root
@app.route('/')

# create function
def hello_world():
    return 'Hello World!'
