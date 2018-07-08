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

    # Comprobamos que todos los datos sean válidos
    if userData is None or userData.account is None or userData.fullname is None or userData.login is None or userData.password is None:
        return "faltan datos en userData", 406

    return 'do some magic!'


def get_user():  # noqa: E501
    """get_user

    Obtiene los datos de un usuario existente # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'
