#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask
from flask_babel import Babel


class Config:
    """Config class for config"""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
