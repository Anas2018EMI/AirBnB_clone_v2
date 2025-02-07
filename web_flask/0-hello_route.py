#!/usr/bin/python3

"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define the route '/' with strict_slashes set to False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles requests to the '/' route.

    Returns:
        str: The message 'Hello HBNB!'
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000)
