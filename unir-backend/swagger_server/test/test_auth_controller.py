# coding: utf-8

from __future__ import absolute_import

from flask import jsonify
from flask import json
from six import BytesIO

from swagger_server.models.credentials import Credentials  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_login_401(self):
        """ Test login sin credenciales """
        credentials = Credentials()
        response = self.client.open(
            '/v1/login',
            method='POST',
            data=json.dumps(credentials),
            content_type='application/json')

           
        self.assert200(response,'Acceso a función sin token')
        self.assertFalse(response.data is None, "La respuesta no es null")

    def test_login_401_2(self):
        """ Test login con contraseña y usuario incorrectas """

        # usu y pass mal
        credentials = Credentials()
        credentials.password = "pass_falsa@@@999)()/*/-"
        credentials.user = "usufalso123123"
        response = self.client.open(
            '/v1/login',
            method='POST',
            data=json.dumps(credentials),
            content_type='application/json')

           
        self.assert401(response,'Acceso a función con credenciales malas')
        self.assertFalse(response.data is None, "La respuesta no es null")

        # usu correcto, pass mal
        credentials = Credentials()
        credentials.password = "pass_falsa@@@999)()/*/-"
        credentials.user = "usupruebas"
        response = self.client.open(
            '/v1/login',
            method='POST',
            data=json.dumps(credentials),
            content_type='application/json')

           
        self.assert401(response,'Acceso a función con credenciales malas')
        self.assertFalse(response.data is None, "La respuesta no es null")

        # usu mal, pass correcta
        credentials = Credentials()
        credentials.password = "123456"
        credentials.user = "usufalso123123"
        response = self.client.open(
            '/v1/login',
            method='POST',
            data=json.dumps(credentials),
            content_type='application/json')

           
        self.assert401(response,'Acceso a función con credenciales malas')
        self.assertFalse(response.data is None, "La respuesta no es null")



    def test_login_200(self):
        """ Test login con credenciales correctas """
        credentials = Credentials()
        credentials.user = "usupruebas"
        credentials.password = "123456"
        
        response = self.client.open(
            '/v1/login',
            method='POST',
            data=json.dumps(credentials),
            content_type='application/json')

           
        self.assert200(response,'Error al hacer login')
        self.assertFalse(response.data is None, "La respuesta no es null")

        return response.data.decode("utf-8").replace("\"","").replace("\n","")

    def test_logout_401(self):
        """ Test logout sin token """

        response = self.client.open(
            '/v1/logout',
            method='DELETE',
            content_type='application/json')
        
        self.assert401(response,'Acceso a función sin token')
        self.assertFalse(response.data is None, "La respuesta no es null")
        
    def test_logout_200(self):
        """ Test logout sin token """

        token = self.test_login_200()
        print("obtenido token: " + token)

        response = self.client.open(
            '/v1/logout',
            method='DELETE',
            content_type='application/json',
            headers={'api_key': token})
        
        self.assert200(response,'Acceso a función sin token')

if __name__ == '__main__':
    import unittest
    unittest.main()
