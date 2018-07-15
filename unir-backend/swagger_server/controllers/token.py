import jwt
import configparser
import swagger_server.controllers.bbdd as bd

from swagger_server.models.credentials import Credentials  # noqa: E501
from json import loads

def check_crentials_token(token):

    secret_key = get_token_secret()
    
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return None
    except jwt.exceptions.DecodeError:
        return None

    return decoded_token["user_id"]
    


def get_token_secret():

    config = configparser.ConfigParser()
    config.read('config.ini')
    secret_key = config['AUTH']['TOKEN_KEY']

    return secret_key
