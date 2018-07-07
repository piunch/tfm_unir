import connexion
import six

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
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
