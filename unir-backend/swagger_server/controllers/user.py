import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_user(login, fullname, password):  # noqa: E501
    """add_user

    Crea un nuevo usuario en la BD # noqa: E501

    :param login: user login
    :type login: str
    :param fullname: user full name
    :type fullname: str
    :param password: user password
    :type password: str

    :rtype: List[User]
    """
    return 'do some magic!'


def get_user():  # noqa: E501
    """get_user

    Obtiene los datos de un usuario existente # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'
