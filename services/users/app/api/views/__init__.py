# users/app/api/views/__init__.py

from flask import Blueprint

user_api = Blueprint('user', __name__)

from .auth import LoginAPI, RegisterAPI, UserAPI

# login view
login_view = LoginAPI.as_view('login_view')
user_api.add_url_rule('/login', view_func=login_view, methods=['POST'])

# register view
register_view = RegisterAPI.as_view('register_view')
user_api.add_url_rule('/register', view_func=register_view, methods=['POST'])

# user view
user_view = UserAPI.as_view('user_view')
user_api.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])
user_api.add_url_rule('/users', view_func=user_view, methods=['GET', 'POST'])

