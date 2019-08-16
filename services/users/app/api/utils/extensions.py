# users/app/api/utils/extensions.py

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

cors = CORS()
bcrypt = Bcrypt()
db = SQLAlchemy()
jwt = JWTManager()
