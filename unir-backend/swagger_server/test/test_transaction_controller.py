# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from time  import sleep

from swagger_server.test.test_auth_controller import TestAuthController
from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_data import TransactionData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransactionController(BaseTestCase):
    """TransactionController integration test stubs"""

    def test_get_balance_401(self):
        """ Test obtener el balance actual """

        response = self.client.open(
            '/v1/balance',
            method='GET',
            content_type='application/json')

        self.assert401(response, 'Error al obtener el balance de forma totalemnte normal')

    def test_get_balance_200(self):
        """ Test obtener el balance actual """
        token = TestAuthController.test_login_200(self)

        response = self.client.open(
            '/v1/balance',
            method='GET',
            content_type='application/json',
            headers={'api_key': token})

        self.assert200(response, 'Error al obtener el balance de forma totalemnte normal')

        return json.loads(response.data.decode('utf-8'))['current_balance']

    def test_add_transaction_401(self):
        """Test case for add_transaction

        
        """
        amount = 100
        previous_balance = self.test_get_balance_200()
        token = "aklasklasl"
        print("amount: " + str(amount) + " balance: " + str(previous_balance))

        transactionData = TransactionData()
        transactionData.amount = amount
        transactionData.description = "Mucho test"

        response = self.client.open(
            '/v1/transaction',
            method='POST',
            data=json.dumps(transactionData),
            content_type='application/json',
            headers={'api_key': token})

        self.assert401(response,'Error al accer una transacción totalemnte normal')

    def test_add_transaction_200_add(self):
        """ Test case for add_transactio """
        # Probamos a añadir dinero
        amount = 100
        previous_balance = self.test_get_balance_200()
        token = TestAuthController.test_login_200(self)
        print("amount: " + str(amount) + " balance: " + str(previous_balance))

        transactionData = TransactionData()
        transactionData.amount = amount
        transactionData.description = "Mucho test"

        response = self.client.open(
            '/v1/transaction',
            method='POST',
            data=json.dumps(transactionData),
            content_type='application/json',
            headers={'api_key': token})
        sleep(.500)

        self.assert200(response,'Error al accer una transacción totalemnte normal')
        
        response_balance = json.loads(response.data.decode('utf-8'))['current_balance']
        new_balance = self.test_get_balance_200()
        expected_balance = previous_balance + amount
        print("expected balance: " + str(expected_balance) + " new balance: " + str(new_balance) + " response balance: " + str(response_balance))

        self.assertEquals(expected_balance,new_balance, "No cuadra la cantidad añadida con el balance actual")
        self.assertEquals(response_balance, expected_balance, "No cuadra la cantidad añadida con el balance esperado")

        # Probamos a quitar dinero
        amount = -100
        previous_balance = self.test_get_balance_200()
        token = TestAuthController.test_login_200(self)
        print("amount: " + str(amount) + " balance: " + str(previous_balance))

        transactionData = TransactionData()
        transactionData.amount = amount
        transactionData.description = "Mucho test"

        response = self.client.open(
            '/v1/transaction',
            method='POST',
            data=json.dumps(transactionData),
            content_type='application/json',
            headers={'api_key': token})
        sleep(.500)

        self.assert200(response,'Error al accer una transacción totalemnte normal')
        
        response_balance = json.loads(response.data.decode('utf-8'))['current_balance']
        new_balance = self.test_get_balance_200()
        expected_balance = previous_balance + amount
        print("expected balance: " + str(expected_balance) + " new balance: " + str(new_balance) + " response balance: " + str(response_balance))

        self.assertEquals(expected_balance,new_balance, "No cuadra la cantidad retirada con el balance actual")
        self.assertEquals(response_balance, expected_balance, "No cuadra la cantidad retirada con el balance esperado")

    def test_get_transactions_401(self):
        """ Test case for get_transactions """

        query_string = [('from_date', 'from_date_example')]

        response = self.client.open(
            '/v1/transaction',
            method='GET',
            content_type='application/json',
            query_string=query_string)

        self.assert401(response,'Acceso a una función sin token')


    def test_get_transactions_200(self):
        """ Test case for get_transactions """

        token = TestAuthController.test_login_200(self)

        response = self.client.open(
            '/v1/transaction',
            method='GET',
            content_type='application/json',
            headers={'api_key': token})

        self.assert200(response,'Error al hacer una petición totalmente normal')

if __name__ == '__main__':
    import unittest
    unittest.main()
