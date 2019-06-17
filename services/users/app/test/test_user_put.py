# users/app/test/test_user_put.py

import json
import unittest

from app.test.base import BaseTestCase
from app.api.models.user import User
from app.api.models.roles import Roles
from app.api.utils.func import (
    save_user, update_user
)


class TestUserPutMethod(BaseTestCase):
    def test_update_email_by_user(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
        )
        user_r = Roles({
            'username': user.username,
            'roles': user.is_admin
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
            response = self.client.put(
                f'/v1/api/users/{user.username}',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'email': 'test@tester.com'
                })
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Updated successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_update_password_by_user(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
        )
        user_r = Roles({
            'username': user.username,
            'roles': user.is_admin
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
            response = self.client.put(
                f'/v1/api/users/{user.username}',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'tester'
                })
            )

            data = json.loads(response.data.decode())
            res = self.client.post(
                '/v1/api/login',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'tester'
                })
            )

            d = json.loads(res.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Updated successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

            self.assertTrue(d['ok'] == True)
            self.assertTrue(d['msg'] == 'Logged in.')
            self.assertTrue(d['access_token'])
            self.assertTrue(res.content_type == 'application/json')
            self.assertEqual(res.status_code, 200)

    def test_update_username_by_user(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
        )
        user_r = Roles({
            'username': user.username,
            'roles': user.is_admin
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
            response = self.client.put(
                f'/v1/api/users/{user.username}',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'tester',
                })
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Cannot change username directly')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    def test_update_email_by_admin(self):
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com'
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

            res_test = self.client.post(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'test',
                    'email': 'test@test.com'
                })
            )

            data_test = json.loads(res_test.data.decode())

            response = self.client.put(
                '/v1/api/users/test',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'email': 'test@tester.com'
                })
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Updated successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_update_password_by_admin(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
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
            response = self.client.put(
                f'/v1/api/users/{user.username}',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'tester'
                })
            )

            data = json.loads(response.data.decode())
            res = self.client.post(
                '/v1/api/login',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'tester'
                })
            )

            d = json.loads(res.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Updated successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

            self.assertTrue(d['ok'] == True)
            self.assertTrue(d['msg'] == 'Logged in.')
            self.assertTrue(d['access_token'])
            self.assertTrue(res.content_type == 'application/json')
            self.assertEqual(res.status_code, 200)

    def test_update_username_by_admin(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
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
            response = self.client.put(
                f'/v1/api/users/{user.username}',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'tester',
                })
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Updated successfully')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_update_invalid_fields_by_admin(self):
        admin = User(
            username='admin',
            password='admin',
            email='admin@admin.com'
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

            res_test = self.client.post(
                '/v1/api/users',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'password': 'test',
                    'email': 'test@test.com'
                })
            )

            data_test = json.loads(res_test.data.decode())

            response = self.client.put(
                '/v1/api/users/test',
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer {}'.format(data_login['access_token'])
                },
                data=json.dumps({
                    'username': 'test',
                    'email': 'test@tester.com',
                    'is_admin': True
                })
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
