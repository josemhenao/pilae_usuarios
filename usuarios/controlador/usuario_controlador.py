from abc import ABC


class UsuarioControlador(ABC):

    @staticmethod
    def is_data_type_validate(usuario):
        if type(usuario.get('id_usuario')) != int:
            return False
        elif type(usuario.get('email')) != str:
            return False
        elif type(usuario.get('password')) != str:
            return False
        elif type(usuario.get('username')) != str:
            return False
        elif type(usuario.get('nombre')) != str:
            return False
        elif type(usuario.get('apellido')) != str:
            return False
        elif type(usuario.get('genero')) != str:
            return False
        elif type(usuario.get('fecha_nacimiento')) != dict:
            return False
        elif type(usuario.get('fecha_nacimiento').get('year')) != int:
            return False
        elif type(usuario.get('fecha_nacimiento').get('month')) != int:
            return False
        elif type(usuario.get('fecha_nacimiento').get('day')) != int:
            return False
        elif type(usuario.get('lugar_nacimiento')) != str:
            return False
        elif type(usuario.get('identificacion')) != str:
            return False
        elif type(usuario.get('imagen')) != str:
            return False
        elif type(usuario.get('rol_id')) != int:
            return False
        else:
            return True










