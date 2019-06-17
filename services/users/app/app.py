# users/app/app.py

import os

from flask import Flask

from app.api.utils.extensions import (
    db, bcrypt, jwt
)
from app.api.utils.func import JSONEncoder

def create_app(app_info=None):
    """Create Flask application in factory pattern
    """

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_SETTINGS'))

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .api.views import user_api as user_bp
    app.register_blueprint(user_bp, url_prefix='/v1/api/')

    app.json_encoder = JSONEncoder

    @app.route('/')
    def index():
        return 'Hello, World'

    return app
