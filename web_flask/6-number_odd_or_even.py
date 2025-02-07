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
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
                          Contains an H1 tag with "Number: n"
                          inside the BODY tag.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
                             Contains an H1 tag with "Number: n is even|odd".
"""

from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Define the route '/' with strict_slashes set to False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles requests to the '/' route."""
    return "Hello HBNB!"

# Define the route '/hbnb' with strict_slashes set to False


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handles requests to the '/hbnb' route."""
    return "HBNB"

# Define the route '/c/<text>' with strict_slashes set to False


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Handles requests to the '/c/<text>' route."""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

# Define the route '/python/<text>' with strict_slashes set to False


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Handles requests to the '/python/<text>' route."""
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

# Define the route '/number/<n>' with strict_slashes set to False


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Handles requests to the '/number/<n>' route."""
    return f"{n} is a number"

# Define the route '/number_template/<n>' with strict_slashes set to False


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Handles requests to the '/number_template/<n>' route."""
    return render_template('5-number.html', number=n)

# Define the route '/number_odd_or_even/<n>' with strict_slashes set to False


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Handles requests to the '/number_odd_or_even/<n>' route.
    Renders an HTML page indicating if the number is odd or even.
    """
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_or_even=odd_or_even)


if __name__ == "__main__":
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000)
