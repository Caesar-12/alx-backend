#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template
from flask_babel import Babel


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
