#!/usr/bin/python3

"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C ' followed by the value of the text variable
               (replace underscore _ symbols with a space)
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

# Define the route '/hbnb' with strict_slashes set to False


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function handles requests to the '/hbnb' route.

    Returns:
        str: The message 'HBNB'
    """
    return "HBNB"

# Define the route '/c/<text>' with strict_slashes set to False


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function handles requests to the '/c/<text>' route.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The message 'C ' followed by the value of the text variable
             with underscores replaced by spaces.
    """
    # Replace underscores with spaces
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


if __name__ == "__main__":
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000)
