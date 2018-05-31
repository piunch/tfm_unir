# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestAuthControllerController(BaseTestCase):
    """AuthControllerController integration test stubs"""

    def test_login(self):
        """Test case for login

        
        """
        data = dict(login='login_example',
                    _pass='_pass_example')
        response = self.client.open(
            '/v1/login',
            method='POST',
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout(self):
        """Test case for logout

        
        """
        response = self.client.open(
            '/v1/logout',
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
