import connexion
import six
import jwt
import configparser
from swagger_server import util
from json import JSONEncoder


def login(credentials):  # noqa: E501
    """login

    Obtiene un token a partir de usuario y contraseña válidos # noqa: E501

    :param credentials: user login
    :type credentials: dict | bytes

    :rtype: str
    """

    # TODO: previamente hay que verificar los datos de login en la BD
    # return '', 401

    # obtenemos la clave, creamos el token con los datos del usuario y lo devolvemos en forma de string
    secret_key = get_token_secret()
    new_token = jwt.encode({'user': 'miaumiaumiau'},
                           secret_key, algorithm='HS256')
    new_token_str = str(new_token)

    return new_token_str, 200


def logout():  # noqa: E501
    """logout

    Revoca un token obtenido con el método /login # noqa: E501


    :rtype: None
    """

    token = connexion.request.headers['api_key']

    secret_key = get_token_secret()
    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])

    return str(decoded_token)


# Other functions


def get_token_secret():

    config = configparser.ConfigParser()
    config.read('config.ini')
    secret_key = config['AUTH']['TOKEN_KEY']

    return secret_key
    