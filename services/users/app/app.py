# users/app/app.py

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(app_info=None):
    """Create Flask application in refactory pattern
    """

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_SETTINGS'))

    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello, World'

    return app
