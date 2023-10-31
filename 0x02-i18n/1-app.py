#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(Babel):
    """Config class for Babel"""
    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)
        
        # Set default locale and timezone here
        self.default_locale = 'en_US'
        self.default_timezone = 'America/New_York'


app = Flask(__name__)
app.config.from_object(Config)

babel = Config()


@app.route('/')
def welcome():
    """homepage"""
    return render_template('0-index.html')
