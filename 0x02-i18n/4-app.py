#!/usr/bin/env python3
"""Force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Best language match"""
    locale_param = request.args.get('locale')

    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return hello world page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
