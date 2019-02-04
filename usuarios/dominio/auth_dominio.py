from abc import ABC
from usuarios.repositorio.usuario_factory import UsuarioFactory
from usuarios.repositorio.auth_factory import AuthFactory

class AuthDominio(ABC):

    @staticmethod
    def login(data):
        session = {}
        return AuthFactory.insert_session(session)

    @staticmethod
    def login(data):
        return UsuarioFactory.insert_usuario(usuario)