from abc import ABC
from usuarios.repositorio.usuario_factory import UsuarioFactory

class UsuarioDominio(ABC):

    @staticmethod
    def create_usuario(data):
        respuesta={}
        created = UsuarioFactory.insert_usuario(usuario)
        return UsuarioFactory.insert_usuario(usuario)

    # @staticmethod
    # def crear_usuarios(usuarios):
    #     return UsuarioFactory.insert_usuarios(usuarios)

    @staticmethod
    def read_usuario(id_usuario):
        return UsuarioFactory.select_usuario(id_usuario)

    @staticmethod
    def read_all_usuarios():
        return UsuarioFactory.select_all_usuarios()

    @staticmethod
    def update_usuario(usuario):
        return UsuarioFactory.update_usuario()

    @staticmethod
    def delete_usuario(id_usuario):
        return UsuarioFactory.delete_usuario(id_usuario)


