import connexion
import six
import swagger_server.controllers.bbdd as bd

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_data import TransactionData  # noqa: E501
from swagger_server.controllers.token import check_crentials_token
from swagger_server import util
from flask import jsonify



def add_transaction(transactionData):  # noqa: E501
    """add_transaction

    Añade una nueva transacción en la cuenta del usuario # noqa: E501

    :param transactionData: transaction amount
    :type transactionData: dict | bytes

    :rtype: Transaction
    """

    if 'api_key' in  connexion.request.headers:
        token = connexion.request.headers['api_key']
    else:
        return "Invalid credentials", 401

    user_id = check_crentials_token(token)
    
    if user_id is None:
        print("Intento de acceso con token incorrecto")
        return "Invalid credentials", 401

    if connexion.request.is_json:
        transactionData = TransactionData.from_dict(connexion.request.get_json())  # noqa: E501

    # Obtenemos la cuenta del usuario
    query = "SELECT ACCOUNTID FROM ACCOUNT WHERE USERID = %s"
    params = (int(user_id),)
    query_result = bd.select(query,params)
    
    if query_result is None or len(query_result) < 1:
        return 'No se encontró el usuario o la cuenta del usuario', 406
    
    account = query_result[0][0]

    if len(transactionData.description) > 128:
        return 'Descripción demasiado larga', 406

    # Insertar la nueva transacción
    query = "INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) SELECT USERID,%s,%s,%s,CURRENTBALANCE + %s,CURRENT_TIMESTAMP FROM TRANSACTIONS WHERE USERID = %s ORDER BY TRANSACTIONDATE DESC LIMIT 1"
    params = (int(account), int(transactionData.amount), str(transactionData.description).upper(), int(transactionData.amount), int(user_id),)
    bd.exec(query,params)

    # formar la query para sacar la nueva transacción
    query = "SELECT ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE,TRANSACTIONID FROM TRANSACTIONS WHERE USERID = %s ORDER BY TRANSACTIONDATE DESC LIMIT 1;"
    params = (int(user_id),)
    query_result = bd.select(query,params)

    if query_result is None or len(query_result) < 1:
        return "No se realizó el insert", 500

    account = query_result[0][0]
    amount = query_result[0][1]
    description = query_result[0][2]
    balance = query_result[0][3]
    date = query_result[0][4]
    transaction_id = query_result[0][5]
    transaction = Transaction(transaction_id, account, amount, description, balance, date)
        
    return jsonify(transaction), 200


def get_balance():  # noqa: E501
    """get_balance

    Obtiene el estado actual de la cuenta del usuario # noqa: E501


    :rtype: Balance
    """

    if 'api_key' in  connexion.request.headers:
        token = connexion.request.headers['api_key']
    else:
        return "Invalid credentials", 401

    user_id = check_crentials_token(token)
    
    if user_id is None:
        print("Intento de acceso con token incorrecto")
        return "Invalid credentials", 401

    # formar la query para sacar la última transacción
    query = "SELECT ACCOUNTID,CURRENTBALANCE,TRANSACTIONDATE FROM TRANSACTIONS WHERE USERID = %s ORDER BY TRANSACTIONDATE DESC LIMIT 1;"
    params = (int(user_id),)
    query_result = bd.select(query,params)

    if query_result is None or len(query_result) < 1:
        return None, 500
    
    # Obtener los datos y crear el objeto para la respuesta
    account_id = query_result[0][0]
    current_balance = query_result[0][1]
    transaction_date = query_result[0][2]
    balance = Balance(account_id, current_balance, transaction_date)

    return jsonify(balance), 200


def get_transactions(from_date=None):  # noqa: E501
    """get_transactions

    Obtiene una lista de las últimas transacciones del usuario # noqa: E501

    :param from_date: from date filter
    :type from_date: str

    :rtype: List[Transaction]
    """

    if 'api_key' in  connexion.request.headers:
        token = connexion.request.headers['api_key']
    else:
        return "Invalid credentials", 401

    user_id = check_crentials_token(token)
    
    if user_id is None:
        print("Intento de acceso con token incorrecto")
        return "Invalid credentials", 401

    if from_date is None:
        query = "SELECT TRANSACTIONID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE FROM TRANSACTIONS WHERE USERID = %s ORDER BY TRANSACTIONDATE DESC;"
        params = (int(user_id),)
    else:
        query = "SELECT TRANSACTIONID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE FROM TRANSACTIONS WHERE USERID = %s AND TRANSACTIONDATE >= %s ORDER BY TRANSACTIONDATE DESC;"
        params = (user_id, from_date,)

    query_result = bd.select(query,params)
    transactions = []

    if query_result is not None:
        for row in query_result:
            id = row[0]
            account = row[1]
            amount = row[2]
            description = row[3]
            balance = row[4]
            date = row[5]

            transaction = Transaction( id, account, amount,  description, balance, date)
            transactions.append(transaction)
    
    return jsonify(transactions), 200
