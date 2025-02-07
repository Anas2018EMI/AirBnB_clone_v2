#!/usr/bin/python3

"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C ' followed by the value of the text variable
               (replace underscore _ symbols with a space)
    /python/<text>: Displays 'Python ' followed by the value of
                     the text variable
                    (replace underscore _ symbols with a space).
                    The default value of text is "is cool".
    /number/<n>: Displays '<n> is a number' only if <n> is an integer.
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
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

# Define the route '/python/<text>' with strict_slashes set to False


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    This function handles requests to the '/python/<text>' route.

    Args:
        text (str): The text provided in the URL. Defaults to 'is cool'.

    Returns:
        str: The message 'Python ' followed by the value of the text variable
             with underscores replaced by spaces.
    """
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

# Define the route '/number/<n>' with strict_slashes set to False


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    This function handles requests to the '/number/<n>' route.

    Args:
        n (int): The integer provided in the URL.

    Returns:
        str: The message '<n> is a number' if <n> is an integer.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000)
