import connexion
import six

from swagger_server import util


def login(login, _pass):  # noqa: E501
    """login

    Obtiene un token a partir de usuario y contraseña válidos # noqa: E501

    :param login: user login
    :type login: str
    :param _pass: user password
    :type _pass: str

    :rtype: str
    """
    return 'do some magic!'


def logout():  # noqa: E501
    """logout

    Revoca un token obtenido con el método /login # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
