from abc import ABC
from usuarios.repositorio.abstract_factory import AbstractFactory
import secrets

class AuthFactory(ABC):
    database = AbstractFactory.get_database()
    database.connect()

    @staticmethod
    def insert_login(*args,**kwargs):
        # Create login procces
        return {'message':'login sucessfull',
                'token':'Token {}'.format(secrets.token_urlsafe())
                }

    @staticmethod
    def remove_login(*args, **kwargs):
        # Create login procces
        return {'message': 'logout sucessfull'}