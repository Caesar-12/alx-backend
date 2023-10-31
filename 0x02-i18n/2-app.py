#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template, request
from flask_babel import Babel, _locale_selector


class Config(Babel):
    """Config class for config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def welcome():
    """homepage"""
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    """deterine best match"""
    return _locale_selector.best_match(app.config['LANGUAGES'],
                                       request.accept_languages)
