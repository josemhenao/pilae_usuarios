from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError


class UsuarioDominio():
    def __init__(self, *args, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.email = kwargs.get('email')
        self.username = kwargs.get('username')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('last_name')
        self.genero = kwargs.get('genero')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
        self.lugar_nacimiento = kwargs.get('lugar_nacimiento')
        self.identificacion = kwargs.get('identificacion')
        self.imagen = kwargs.get('imagen') or 'hola'
        self.grupo = kwargs.get('grupo')

        if kwargs.get('password')is not None:
            self.password = self.hash_password(kwargs.get('password'))

    def to_dict(self):
        return { 'id_usuario' : self.id_usuario,
                 'email' : self.email,
                 #'password' : self.password, # Never return this
                 'username' : self.username,
                 'nombre' : self.nombre,
                 'apellido' : self.apellido,
                 'genero' : self.genero,
                 'fecha_nacimiento' : self.fecha_nacimiento,
                 'lugar_nacimiento' : self.lugar_nacimiento,
                 'identificacion' : self.identificacion,
                 'imagen' : self.imagen,
                 'grupo' : self.grupo.to_dict()
                 }

    def hash_password(self, raw_password):
        ph = PasswordHasher()
        hash = ph.hash(raw_password)
        return hash

    def verify_password(self, raw_password):
        ph = PasswordHasher()
        is_equals = False
        try:
            is_equals = ph.verify(self.password, raw_password)
        except VerifyMismatchError:
            print(VerifyMismatchError)
        except VerificationError:
            print(VerificationError)
        finally:
            is_equals = False

        return is_equals

    def __repr__(self):
        return self.username

class GrupoDominio():
    def __init__(self, *args, **kwargs):
        self.id_grupo = kwargs.get('id_grupo')
        self.grupo = kwargs.get('grupo')
        self.descripcion = kwargs.get('descripcion')

        if kwargs.get('recursos') is not None:
            self.recursos = [RecursoDominio(**recurso) for recurso in kwargs.get('recursos')]

    def to_dict(self):
        return {'id_grupo' : self.id_grupo,
                'grupo' : self.grupo,
                'descripcion' : self.descripcion
                }

class RecursoDominio():
    def __init__(self, *args, **kwargs):
        self.id_recurso = kwargs.get('id_recurso')
        self.recurso = kwargs.get('recurso')
        self.descripcion = kwargs.get('descripcion')

    def to_dict(self):
        return {'id_recurso' : self.id_recurso,
                'recurso' : self.recurso,
                'descripcion' : self.descripcion
                }



# josemJSON = {'username':'josemhenao',
#              'email':'josem.henao@gmail.com',
#              'password':'josemhenao123',
#              'nombre':'José Miguel',
#              'apellido':'Henao',
#              'grupo':{'id_grupo':1,
#                       'grupo':'Administrador'},
#              'otros_1':'otros atributos 1'
#              }
# josem = UsuarioDTO(**josemJSON)
# print(josem.__dict__)
# print(josem.verify_password('josemhenao123123'))