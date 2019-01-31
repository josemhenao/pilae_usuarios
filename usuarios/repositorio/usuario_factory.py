from abc import ABC, abstractmethod
from usuarios.repositorio.abstract_factory import AbstractFactory

class UsuarioFactory(ABC):
    database = AbstractFactory.get_database()
    database.connect()

    @staticmethod
    def insert_usuario(usuario):
        return {
            'mensaje': 'Se ha insertado un usuario'
        }

    @staticmethod
    def insert_usuarios(usuarios):
        return {
            'mensaje': 'Se han insertado varios usuarios'
        }

    @staticmethod
    def select_usuario(id_usuario):
        return {
            'mensaje': 'Se ha seleccionado el usuario con id:{}'.format(id_usuario)
        }

    @staticmethod
    def select_all_usuarios():
        return {
            'usuario_1':{
                'nombre':'José Miguel',
                'apellido':'Henao'
            },'usuario_2':{
                'nombre': 'Juan José',
                'apellido': 'Giraldo'
            }
        }

    @staticmethod
    def update_usuario(usuario):
        return {
            'mensaje': 'Se ha actualizado el usuario con id:{}'.format(usuario.get['id_usuario'])
        }

    @staticmethod
    def delete_usuario(id_usuario):
        return {
            'mensaje':'Se ha eliminado el usuario con id:{}'.format(id_usuario)
        }


