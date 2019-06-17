# users/app/test/test_user_get.py

import json
import unittest

from app.test.base import BaseTestCase
from app.api.models.user import User
from app.api.models.roles import Roles
from app.api.utils.func import (
    save_user, update_user
)


class TestUserGetMethod(BaseTestCase):
    def test_get_all_users_with_no_jwt(self):
        user = User(
            username='test',
            password='test',
            email='email@email.com',
        )
        role = Roles({
            'username': user.username,
            'roles': user.is_admin
        })
        save_user(user)
        save_user(role)

        with self.client:
            response = self.client.get(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Sorry, page not found.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_get_admin_users_with_no_jwt(self):
        user = User(
            username='test',
            password='test',
            email='email@email.com',
        )
        role = Roles({
            'username': user.username,
            'roles': user.is_admin
        })
        save_user(user)
        save_user(role)

        with self.client:
            response = self.client.get(
                '/v1/api/users/admin',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Sorry, page not found.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_get_all_users_with_unauthorized_jwt(self):
        user = User(
            username='test',
            password='test',
            email='email@email.com',
        )
        role = Roles({
            'username': user.username,
            'roles': user.is_admin
        })
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com',
        )
        admin_r = Roles({
            'username': admin.username,
            'roles': admin.is_admin
        })
        save_user(user)
        save_user(role)
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
                    'username': 'test',
                    'password': 'test'
                })
            )
            data_login = json.loads(res_login.data.decode())

            response = self.client.get(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Sorry, page not found.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_get_admin_user_with_unauthorized_jwt(self):
        user = User(
            username='test',
            password='test',
            email='email@email.com',
        )
        role = Roles({
            'username': user.username,
            'roles': user.is_admin
        })
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com',
        )
        admin_r = Roles({
            'username': admin.username,
            'roles': admin.is_admin
        })
        save_user(user)
        save_user(role)
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
                    'username': 'test',
                    'password': 'test'
                })
            )
            data_login = json.loads(res_login.data.decode())

            response = self.client.get(
                '/v1/api/users/admin',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Sorry, page not found.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_get_all_users_with_authorized_jwt(self):
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com',
        )
        admin_r = Roles({
            'username': admin.username,
            'roles': admin.is_admin
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

            response = self.client.get(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Accessed to admin page.')
            self.assertTrue(data['data'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_get_admin_user_with_authorized_jwt(self):
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com',
        )
        admin_r = Roles({
            'username': admin.username,
            'roles': admin.is_admin
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

            response = self.client.get(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Accessed to admin page.')
            self.assertTrue(data['data'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_get_user_with_own_jwt(self):
        user = User(
            username='test',
            password='test',
            email='email@email.com',
        )
        role = Roles({
            'username': user.username,
            'roles': user.is_admin
        })
        save_user(user)
        save_user(role)

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

            response = self.client.get(
                '/v1/api/users/{}'.format(user.username),
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Accessed to my page.')
            self.assertTrue(data['is_user'] == True)
            self.assertTrue(data['data'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_get_user_with_other_jwt(self):
        user = User(
            username='test',
            password='test',
            email='email@email.com',
        )
        role = Roles({
            'username': user.username,
            'roles': user.is_admin
        })
        save_user(user)
        save_user(role)

        me = User(
            username='me',
            password='me',
            email='me@me.com',
        )
        role_me = Roles({
            'username': me.username,
            'roles': me.is_admin
        })
        save_user(me)
        save_user(role_me)

        with self.client:
            res_login = self.client.post(
                '/v1/api/login',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                data=json.dumps({
                    'username': 'me',
                    'password': 'me'
                })
            )
            data_login = json.loads(res_login.data.decode())

            response = self.client.get(
                '/v1/api/users/{}'.format(user.username),
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                }
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(
                data['msg'] == 'Accessed to {} page.'.format(user.username))
            self.assertTrue(data['is_user'] == False)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
