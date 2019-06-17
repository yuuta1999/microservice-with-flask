# users/app/test/test_user_post.py

import json
import unittest

from app.test.base import BaseTestCase
from app.api.models.user import User
from app.api.models.roles import Roles
from app.api.utils.func import (
    save_user, update_user
)

class TestUserPostMethod(BaseTestCase):
    def test_post_non_admin_user_with_admin_user(self):
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com',
        )
        admin_r = Roles({
            'username': admin.username,
            'roles': admin.roles
        })
        save_user(admin)
        save_user(admin_r)
        with self.client:
            res_login = self.client.post(
                '/v1/api/login',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                data=json.dumps({
                    'username': 'admin',
                    'password': 'admin'
                })
            )
            data_login = json.loads(res_login.data.decode())

            response = self.client.post(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'local',
                    'password': 'local',
                    'email': 'local@localhost.com',
                })
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Registered successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code == 201)

    def test_post_non_admin_user_with_admin_role(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com',
        )
        user_r = Roles({
            'username': user.username,
            'roles': 'admin'
        })
        save_user(user)
        save_user(user_r)
        with self.client:
            res_login = self.client.post(
                '/v1/api/login',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'test'
                })
            )
            data_login = json.loads(res_login.data.decode())

            response = self.client.post(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'local',
                    'password': 'local',
                    'email': 'local@localhost.com',
                })
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Registered successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code == 201)

if __name__ == '__main__':
    unittest.main()
