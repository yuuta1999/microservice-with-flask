# users/app/views/auth.py

import datetime

from flask.views import MethodView
from flask import request, make_response, jsonify, current_app
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity, current_user,
    jwt_optional, jwt_required
)

from ..models.user import User, Roles
from ..utils.func import (
    get_user_by_username, get_user_by_email, get_all_user,
    verify_bcrypt_pwd,
    update_user, delete_user, save_user
)
from app.api.schemas import user_schema
from app.api.utils.extensions import jwt

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
                'msg': 'Incorrect username or password. Please try again.',
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
            return make_response(jsonify(res)), 403
        
        access_token_time = datetime.timedelta(minutes=current_app.config.get('ACCESS_TOKEN_EXPIRE'))
        access_token = create_access_token(
            identity=user.username,
            expires_delta=access_token_time
        )

        res = {
            'ok': True,
            'access_token': access_token,
            'msg': 'Logged in.',
            'data': user
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

        if not user and not get_user_by_email(email, User):
            new_user = User(
                username=username,
                email=email,
                password=password
            )
            new_role = Roles({
                'username': new_user.username,
                'roles': 'user' if new_user.is_admin == False else 'admin'
            })
            save_user(user_obj=new_user)
            save_user(new_role)
            
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
    @jwt_optional
    def get(self, username=None):
        current_user = get_jwt_identity()
        res = {}


        if username is None or username == 'admin':
            if current_user == 'admin':
                res = {
                    'ok': True,
                    'msg': 'Accessed to admin page.',
                    'data': get_all_user(User)
                }
                return make_response(jsonify(res)), 200
            else:
                res = {
                    'ok': False,
                    'msg': 'Sorry, page not found.'
                }
                return make_response(jsonify(res)), 404
        else:
            if current_user == username:
                res = {
                    'ok': True,
                    'msg': 'Accessed to my page.',
                    'is_user': True,
                    'data': get_user_by_username(username, User).to_json()
                }
                return make_response(jsonify(res)), 200
            else:
                res = {
                    'ok': True,
                    'msg': 'Accessed to {} page.'.format(username),
                    'is_user': False
                }
                return make_response(jsonify(res)), 200

    @jwt_required
    def post(self):
        """POST method for admin roles only. 
        """
        if current_user.username != 'admin' and current_user.roles != 'admin':
            return make_response(jsonify({
                'ok': False,
                'msg': 'User is unauthorized'
            })), 401

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

        if not user and not get_user_by_email(email, User):
            new_user = User(
                username=username,
                email=email,
                password=password
            )
            new_role = Roles({
                'username': new_user.username,
                'roles': 'user' if new_user.is_admin == False else 'admin'
            })
            save_user(user_obj=new_user)
            save_user(user_obj=new_role)

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

    @jwt_required
    def put(self, username):
        if current_user.username not in (username, 'admin') and current_user.roles != 'admin':
            return make_response(jsonify({
                'ok': False,
                'msg': 'Method is not allowed'
            })), 405

        req = request.get_json()
        res = {}

        data, err = user_schema.load(req, partial=True)
        allowed_fields = ('username', 'password', 'email')

        not_allowed_fields = list(set(data) - set(allowed_fields))

        if err:
            res = {
                'ok': False,
                'msg': err
            }
            return make_response(jsonify(res)), 400

        if len(not_allowed_fields) != 0:
            res = {
                'ok': False,
                'msg': 'Unknown known fields: {}'.format(' '.join(not_allowed_fields))
            }
            return make_response(jsonify(res)), 400

        if 'username' in data and 'admin' not in list(vars(current_user).values()):
            if current_user.username != data.get('username'):
                res = {
                    'ok': False,
                    'msg': 'Cannot change username directly'
                }
                return make_response(jsonify(res)), 401

        try:
            user_obj = get_user_by_username(current_user.username, User)

            if data.get('username') != username:
                update_user(user_obj, data)

            else:
                d = dict([(k,v) for k,v in data.items() if k != 'username'])
                update_user(user_obj, d)

            res = {
                'ok': True,
                'msg': 'Updated successfully'
            }
            return make_response(jsonify(res)), 200
        except Exception as e:
            res = {
                'ok': False,
                'msg': '{}'.format(e)
            }
            return make_response(jsonify(res)), 500

    @jwt_required
    def delete(self, username):
        if 'admin' not in (current_user.username, current_user.roles):
            return make_response(jsonify({
                'ok': False,
                'msg': 'Method is not allowed'
            })), 405

        user = get_user_by_username(username, User)

        delete_user(user)
        return make_response(jsonify({
            'ok': True,
            'msg': 'Deleted successfully'
        })), 204


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    if get_user_by_username(identity, User) is None:
        return None

    return get_user_by_username(identity, Roles)
