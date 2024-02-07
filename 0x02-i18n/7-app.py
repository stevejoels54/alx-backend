#!/usr/bin/env python3
"""Mock logging in"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from typing import Union, Dict


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id) -> Union[Dict, None]:
    """Retrieve a user"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set the logged-in user"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    locale_param = request.args.get('locale')
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    request_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if request_locale:
        return request_locale

    return app.config['BABEL_DEFAULT_LOCALE']


def validate_timezone(timezone: str) -> Union[str, None]:
    """Validate timezone and return it if valid, otherwise return None."""
    try:
        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return None

@babel.timezoneselector
def get_timezone():
    """Get timezone"""
    timezone_param = request.args.get('timezone')
    if timezone_param:
        validated_timezone = validate_timezone(timezone_param)
        if validated_timezone:
            return validated_timezone

    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            validated_timezone = validate_timezone(user_timezone)
            if validated_timezone:
                return validated_timezone

    return 'UTC'


@app.route('/')
def index():
    """Return logged in user"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
