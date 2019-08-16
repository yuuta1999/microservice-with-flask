# users/app/app.py

import os

from flask import Flask

from app.api.utils.extensions import (
    db, bcrypt, jwt, cors
)
from app.api.utils.func import JSONEncoder

def create_app(app_info=None):
    """Create Flask application in factory pattern
    """

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_SETTINGS'))

    cors.init_app(app, origins=app.config.get('CORS_ORIGINS'), supports_credentials=True)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .api.views import user_api as user_bp
    app.register_blueprint(user_bp, url_prefix='/v1/')

    app.json_encoder = JSONEncoder

    @app.route('/')
    def index():
        return 'Hello, World'

    return app
