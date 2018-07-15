# coding: utf-8

from __future__ import absolute_import

import calendar
import time

from flask import json
from six import BytesIO

from swagger_server.test.test_auth_controller import TestAuthController
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_register_data import UserRegisterData  # noqa: E501
from swagger_server.test import BaseTestCase

class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_get_user_401(self):
        """Test case for get_user

        
      """
        response = self.client.open(
            '/v1/user',
            method='GET',
            content_type='application/json')

        self.assert401(response,'Acceso a función sin token')

    def test_get_user_200(self):
        """ Test case for get_user """
        
        token = TestAuthController.test_login_200(self)

        response = self.client.open(
            '/v1/user',
            method='GET',
            content_type='application/json',
            headers={'api_key': token})

        self.assert200(response,'Error al obtener los datos del usuario')

    def test_add_user_406(self):
        """Test case for add_user"""

        userData = UserRegisterData()

        response = self.client.open(
            '/v1/user',
            method='POST',
            data=json.dumps(userData),
            content_type='application/json')

        self.assertEquals(response.status_code, 406, 'Se creó un usuario sin datos!')

    def test_add_user_200(self):
        """Test case for add_user"""

        userData = UserRegisterData()
        userData.login = "ut"+ str(calendar.timegm(time.gmtime()))
        userData.fullname = "usutest usutest usutest"
        userData.account = "ES123456"
        userData.password = "654321"

        print("login: " + userData.login +" fullname: \"" + userData.fullname + "\" account: \""+ userData.account + "\" password: \"" + userData.password + "\"")

        response = self.client.open(
            '/v1/user',
            method='POST',
            data=json.dumps(userData),
            content_type='application/json')

        print(str(response.data.decode('utf-8')))
        self.assert200(response,'Error al crear un usuario totalmente normal ')




if __name__ == '__main__':
    import unittest
    unittest.main()

