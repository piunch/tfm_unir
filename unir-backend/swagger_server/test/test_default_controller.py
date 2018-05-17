# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_transaction(self):
        """Test case for add_transaction

        
        """
        data = dict(aumount='aumount_example',
                    description='description_example')
        response = self.client.open(
            '/v1/transaction',
            method='POST',
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_get_balance(self):
        """Test case for get_balance

        
        """
        response = self.client.open(
            '/v1/balace',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transactions(self):
        """Test case for get_transactions

        
        """
        query_string = [('from_date', 'from_date_example')]
        response = self.client.open(
            '/v1/transaction',
            method='GET',
            content_type='application/json',
            query_string=query_string)
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
