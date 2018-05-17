import connexion
import six

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_transaction(aumount, description=None):  # noqa: E501
    """add_transaction

    Añade una nueva transacción en la cuenta del usuario # noqa: E501

    :param aumount: transaction amount
    :type aumount: str
    :param description: transaction description
    :type description: str

    :rtype: Transaction
    """
    return 'do some magic!'


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


def get_balance():  # noqa: E501
    """get_balance

    Obtiene el estado actual de la cuenta del usuario # noqa: E501


    :rtype: Balance
    """
    return 'do some magic!'


def get_transactions(from_date=None):  # noqa: E501
    """get_transactions

    Obtiene una lista de las últimas transacciones del usuario # noqa: E501

    :param from_date: from date filter
    :type from_date: str

    :rtype: List[Transaction]
    """
    return 'do some magic!'


def get_user():  # noqa: E501
    """get_user

    Obtiene los datos de un usuario existente # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


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
