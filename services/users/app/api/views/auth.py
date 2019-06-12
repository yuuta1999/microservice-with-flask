# users/app/views/auth.py

import datetime

from flask.views import MethodView
from flask import request, make_response, jsonify, current_app
from flask_jwt_extended import create_access_token

from ..models.user import User
from ..utils.func import (
    get_user_by_username,
    verify_bcrypt_pwd,
    update_user, delete_user, save_user
)
from ..schemas import user_schema

class LoginAPI(MethodView):
    """Login endpoint
    """
    def post(self):
        '''Get data from request.
        '''
        req = request.get_json()
        res = {}

        data, err = user_schema.load(req, partial=True)

        if err:
            res = {
                'ok': False,
                'msg': err
            }
            return make_response(jsonify(res)), 400

        username = data.get('username')
        password = data.get('password')

        user = get_user_by_username(username, User)

        if not user:
            res = {
                'ok': False,
                'msg': 'Incorrect username or password. Please try again.'
            }
            return make_response(jsonify(res)), 400
        elif not verify_bcrypt_pwd(user.password, password):
            res = {
                'ok': False,
                'msg': 'Incorrect username or password. Please try again.'
            }
            return make_response(jsonify(res)), 400
        elif not user.is_active:
            res = {
                'ok': False,
                'msg': 'User is currently banned! Please recover.'
            }
            return make_response(jsonify(res)), 400
        
        access_token_time = datetime.timedelta(minutes=current_app.config.get('ACCESS_TOKEN_EXPIRE'))
        access_token = create_access_token(
            identity=user.username,
            expires_delta=access_token_time
        )

        res = {
            'ok': True,
            'access_token': access_token,
            'msg': 'Logged in.'
        }
        return make_response(jsonify(res)), 200

class RegisterAPI(MethodView):
    """Register endpoint
    """
    def post(self):
        req = request.get_json()
        res = {}

        data, err = user_schema.load(req)

        if err:
            res = {
                'ok': False,
                'msg': err
            }
            return make_response(jsonify(res)), 400

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        user = get_user_by_username(username, User)

        if not user:
            new_user = User(
                username=username,
                email=email,
                password=password
            )
            save_user(user_obj=new_user)
            
            res = {
                'ok': True,
                'msg': 'Registered successfully'
            }
            return make_response(jsonify(res)), 201

        else:
            res = {
                'ok': False,
                'msg': 'User has existed already'
            }
            return make_response(jsonify(res)), 400

class UserAPI(MethodView):
    """Read users
    """
    def get(self, user_id=None):
        pass

    def post(self):
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass
