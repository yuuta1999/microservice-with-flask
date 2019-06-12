# users/app/test/test_auth.py

import json
import unittest

from app.test.base import BaseTestCase
from app.api.models.user import User
from app.api.utils.func import (
    save_user
)

class TestAuthentication(BaseTestCase):
    """Testing authentication service
    """
    def test_login(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
        )
        save_user(user)
        with self.client:
            response = self.client.post(
                '/v1/api/login',
                data=json.dumps({
                    'username': 'test',
                    'password': 'test'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == True)
            self.assertTrue(data['msg'] == 'Logged in.')
            self.assertTrue(data['access_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_login_with_wrong_pwd(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
        )
        save_user(user)
        with self.client:
            response = self.client.post(
                '/v1/api/login',
                data=json.dumps({
                    'username': 'test',
                    'password': '123'
                }),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Incorrect username or password. Please try again.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)
        
    def test_login_with_wrong_username(self):
        user = User(
            username='test',
            password='test',
            email='test@test.com'
        )
        save_user(user)

        with self.client:
            response = self.client.post(
                '/v1/api/login',
                data=json.dumps({
                    'username': 'test1',
                    'password': 'test'
                }),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())

            self.assertTrue(data['ok'] == False)
            self.assertTrue(data['msg'] == 'Incorrect username or password. Please try again.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
