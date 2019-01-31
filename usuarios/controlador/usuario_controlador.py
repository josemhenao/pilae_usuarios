from abc import ABC


class UsuarioControlador(ABC):

    @staticmethod
    def validate_data(usuarios:dict):
        pass

    @staticmethod
    def home_GET():
        return 'home!, use a valid url...'






