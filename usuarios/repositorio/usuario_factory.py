from abc import ABC, abstractmethod
from usuarios.repositorio.abstract_factory import AbstractFactory
from .models import Usuario
from peewee import IntegrityError, DoesNotExist

class UsuarioFactory(ABC):
    database = AbstractFactory.get_database()
    database.connect()

    @staticmethod
    def insert_usuario(usuario):
        try:
            new_usuario = Usuario(**usuario)
            new_usuario.save()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def select_usuario(id_usuario):
        user = None
        try:
            user = Usuario.get(id_usuario=id_usuario).to_dict()
        except IndexError:
            print(IndexError)
        except DoesNotExist:
            print(DoesNotExist)

        print(user)
        return user

    @staticmethod
    def select_all_usuarios():
        usuarios = None
        try:
            usuarios = [u.to_dict() for u in Usuario.select()]
        except DoesNotExist:
            print(DoesNotExist)
        except IndexError:
            print(IndexError)
        except Exception:
            print(Exception)
        return usuarios

    @staticmethod
    def update_usuario(usuario):
        return None

    @staticmethod
    def delete_usuario(id_usuario):
        eliminated = False
        try:
            Usuario.delete_by_id(id_usuario)
            eliminated = True
        except:
            pass
        return eliminated


