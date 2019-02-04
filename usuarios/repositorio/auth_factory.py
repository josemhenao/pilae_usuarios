from abc import ABC
from usuarios.repositorio.abstract_factory import AbstractFactory
from .models import Session
import secrets

class AuthFactory(ABC):
    database = AbstractFactory.get_database()
    database.connect()

    @staticmethod
    def insert_login(*args,**kwargs):
        try:
            session = Session(**kwargs)
            session.save()
        except e:
            print(e)
        finally:
            database.close()


    @staticmethod
    def remove_login(*args, **kwargs):
        # Create login procces
        return {'message': 'logout sucessfull'}