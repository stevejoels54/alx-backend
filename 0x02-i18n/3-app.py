#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Best language match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return hello world page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)