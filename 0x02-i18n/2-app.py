#!/usr/bin/env python3
""" Module for task 2
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config object for Flask Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Babel Locale selector
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def get_index() -> str:
    """ Get the index page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
