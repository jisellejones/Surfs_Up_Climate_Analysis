# Import dependency
from flask import Flask

# Create new flask instance
app = Flask(__name__)

# Define starting point for route
@app.route("/")
def hello_world():
    return "This is awesome!"
    