from abc import ABC
from usuarios.repositorio.usuario_factory import UsuarioFactory

class AuthDominio(ABC):

    @staticmethod
    def login(data):
        return UsuarioFactory.insert_usuario(usuario)

    @staticmethod
    def login(data):
        return UsuarioFactory.insert_usuario(usuario)