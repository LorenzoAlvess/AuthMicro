# coding: utf-8

"""
    Autenticação de Usuário API

    API que gerencia a autenticação e autorização de usuários.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_forgot_password_post(self):
        """Test case for auth_forgot_password_post

        Envia um e-mail com um token exclusivo para redefinir a senha do usuário.  # noqa: E501
        """
        pass

    def test_auth_login_post(self):
        """Test case for auth_login_post

        Autentica o usuário e retorna um token de acesso.  # noqa: E501
        """
        pass

    def test_auth_register_post(self):
        """Test case for auth_register_post

        Cria uma nova conta de usuário no sistema.  # noqa: E501
        """
        pass

    def test_auth_update_user_put(self):
        """Test case for auth_update_user_put

        Altera os dados de login do usuário autenticado.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
