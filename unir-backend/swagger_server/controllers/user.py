import connexion
import six
import swagger_server.controllers.bbdd as bd
import hashlib

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_register_data import UserRegisterData  # noqa: E501
from swagger_server.controllers.token import check_crentials_token
from swagger_server import util
from flask import jsonify


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


    if len(userData.account) > 64:
        return "nombre de cuenta demasiado largo (max 64)", 406
    
    if len(userData.fullname) > 64:
        return "nombre de cuenta demasiado largo (max 64)", 406
    
    if len(userData.login) > 16:
        return "nombre de cuenta demasiado largo (max 16)", 406

    if len(userData.password) < 3:
        return "contraseña demasiado corta (min 3)", 406

    # pasasr la contraseña a sha512
    hash_object = hashlib.sha512(userData.password.encode('utf-8'))
    sha_512 = str(hash_object.hexdigest()).upper()

    # Comprobar que el login está disponible 
    query = "SELECT FULLNAME FROM USER WHERE USERNAME = %s"
    params = (userData.login.upper(),)
    query_result = bd.select(query, params)

    if query_result is None or len(query_result) > 0:
        return 'Ya existe un usuario con ese login', 406

    # insertar en BD al nuevo usuario
    query = "INSERT INTO USER (USERNAME,FULLNAME,PASSWORD,CREATIONDATE) VALUES (%s,%s,%s,CURRENT_TIMESTAMP);"
    params = (userData.login.upper(), userData.fullname.upper(), sha_512,)
    bd.exec(query,params)


    # Obtenemos los datos del usuario para verificar la inserción 
    query = "SELECT FULLNAME, USERID, USERNAME FROM USER WHERE USERNAME = %s"
    params = (userData.login.upper(),)
    query_result = bd.select(query, params)

    if query_result is None or len(query_result) < 1:
        return 'No se encontró el usuario', 406

    fullname = query_result[0][0]
    user_id = query_result[0][1]
    login = query_result[0][2]
    user_data = User(user_id, login, fullname)

    #si se ha insertado el usuario, le creamos una cuenta
    query = "INSERT INTO ACCOUNT (ACCOUNTNUMBER,USERID) VALUES (%s,%s);"
    params = (str(userData.account).upper(), int(user_id),)
    bd.exec(query,params)    

    
    # Insertar la nueva transacción
    query = "INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) SELECT USERID,ACCOUNTID,0,'APERTURA DE CUENTA',0,CURRENT_TIMESTAMP FROM ACCOUNT WHERE USERID = %s"
    params = (int(user_id),)
    bd.exec(query,params)

    return jsonify(user_data)

def get_user():  # noqa: E501
    """get_user

    Obtiene los datos de un usuario existente # noqa: E501


    :rtype: List[User]
    """

    if 'api_key' in  connexion.request.headers:
        token = connexion.request.headers['api_key']
    else:
        return "Invalid credentials", 401

    user_id = check_crentials_token(token)
    
    if user_id is None:
        print("Intento de acceso con token incorrecto")
        return "Invalid credentials", 401

    # Obtenemos los datos del usuario
    query = "SELECT FULLNAME, USERID, USERNAME FROM USER WHERE USERID = %s"
    params = (int(user_id),)
    query_result = bd.select(query,params)

    if query_result is None or len(query_result) < 1:
        return 'No se encontró el usuario', 406

    fullname = query_result[0][0]
    user_id = query_result[0][1]
    login = query_result[0][2]
    user_data = User(user_id,login,fullname)

    return jsonify(user_data)
