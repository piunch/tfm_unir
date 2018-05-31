# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserControllerController(BaseTestCase):
    """UserControllerController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        
        """
        data = dict(login='login_example',
                    fullname='fullname_example',
                    password='password_example')
        response = self.client.open(
            '/v1/user',
            method='POST',
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        
        """
        response = self.client.open(
            '/v1/user',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
