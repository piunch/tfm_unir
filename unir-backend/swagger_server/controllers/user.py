import connexion
import six


from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_register_data import UserRegisterData  # noqa: E501
from swagger_server import util


def add_user(userData):  # noqa: E501
    """add_user

    Crea un nuevo usuario en la BD # noqa: E501

    :param userData: user login
    :type userData: dict | bytes

    :rtype: List[User]
    """
    if connexion.request.is_json:
        userData = UserRegisterData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user():  # noqa: E501
    """get_user

    Obtiene los datos de un usuario existente # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'
