import connexion
import six
import jwt
import configparser
import swagger_server.controllers.bbdd as bd
import hashlib

from swagger_server.controllers.token import check_crentials_token, get_token_secret
from  swagger_server.models.credentials import Credentials
from swagger_server import util
from random import randint, seed
from json import JSONEncoder,loads
from time import clock


def login(credentials):  # noqa: E501
    """login

    Obtiene un token a partir de usuario y contraseña válidos # noqa: E501

    :param credentials: user login
    :type credentials: dict | bytes

    :rtype: str
    """
    
    # obtener los datos del json
    if connexion.request.is_json:
        credentials = Credentials.from_dict(connexion.request.get_json())

    # Convertir la contraseña a sha512
    hash_object = hashlib.sha512(credentials.password.encode('utf-8'))
    sha_512 = str(hash_object.hexdigest()).upper()

    # Comprobamos las credenciales en BD y nos quedamos con la id
    query = "SELECT USERID FROM USER WHERE USERNAME = %s AND PASSWORD = %s"
    params = ( str(credentials.user).upper(), sha_512,)
    query_result = bd.select(query, params)

    if query_result is None or len(query_result) < 1:
        return 'Las credenciales no coinciden con usuario alguno', 401
    
    user_id = query_result[0][0]
    
    # obtenemos la clave, creamos el token con los datos del usuario y lo devolvemos en forma de string
    secret_key = get_token_secret()
    seed(clock())
    new_token = jwt.encode({'user': str(credentials.user),
                            'user_id': str(user_id),
                            'key': str(sha_512),
                            'rand': str(randint(0, 99999999999))},
                           secret_key, algorithm='HS256')

    new_token_str = str(new_token.decode("utf-8"))
    return new_token_str, 200


def logout():  # noqa: E501
    """logout

    Revoca un token obtenido con el método /login # noqa: E501


    :rtype: None
    """

    token = connexion.request.headers['api_key']
    user_id = check_crentials_token(token)
    
    if user_id is None:
        print("Intento de acceso con token incorrecto")
        return "Invalid credentials", 401

    return "OK", 200


# Other functions



    