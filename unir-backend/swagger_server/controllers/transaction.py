import connexion
import six
import swagger_server.controllers.bbdd as bd

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_data import TransactionData  # noqa: E501
from swagger_server import util
from flask import jsonify


def add_transaction(transactionData):  # noqa: E501
    """add_transaction

    Añade una nueva transacción en la cuenta del usuario # noqa: E501

    :param transactionData: transaction amount
    :type transactionData: dict | bytes

    :rtype: Transaction
    """
    if connexion.request.is_json:
        transactionData = TransactionData.from_dict(connexion.request.get_json())  # noqa: E501

    query = "INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) VALUES (1,%s,%s,%s,%s,%s);"
    
    return 'do some magic!'
11

def get_balance():  # noqa: E501
    """get_balance

    Obtiene el estado actual de la cuenta del usuario # noqa: E501


    :rtype: Balance
    """

    user_id = 1

    # formar la query para sacar la última transacción
    query = "SELECT ACCOUNTID,CURRENTBALANCE,TRANSACTIONDATE FROM TRANSACTIONS WHERE USERID = %s ORDER BY TRANSACTIONDATE DESC LIMIT 1;"
    params = (int(user_id),)
    query_result = bd.exec(query,params)

    if query_result is None or len(query_result) < 1:
        return jsonify(Balance())
    
    # Obtener los datos y crear el objeto para la respuesta
    account_id = query_result[0][0]
    current_balance = query_result[0][1]
    transaction_date = query_result[0][2]
    balance = Balance(account_id, current_balance, transaction_date)

    return jsonify(balance)


def get_transactions(from_date=None):  # noqa: E501
    """get_transactions

    Obtiene una lista de las últimas transacciones del usuario # noqa: E501

    :param from_date: from date filter
    :type from_date: str

    :rtype: List[Transaction]
    """

    user_id = 1

    if from_date is None:
        query = "SELECT RANSACTIONID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE FROM TRANSACTIONS WHERE USERID = %s ORDER BY TRANSACTIONDATE DESC;"
        params = (user_id,)
    else:
        query = "SELECT TRANSACTIONID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE FROM TRANSACTIONS WHERE USERID = %s AND TRANSACTIONDATE >= %s ORDER BY TRANSACTIONDATE DESC;"
        params = (user_id, from_date,)

    query_result = bd.exec(query,params)
    transactions = []

    for row in query_result:
        id = row[0]
        account = row[1]
        amount = row[2]
        description = row[3]
        balance = row[4]
        date = row[5]

        transaction = Transaction( id, account, amount, description, balance, date)
        transactions.append(transaction)
    
    return jsonify(transactions)
