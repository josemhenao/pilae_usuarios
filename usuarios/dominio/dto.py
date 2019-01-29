
class UsuarioDTO():
    def __init__(self, *args, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.username = kwargs.get('username')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('last_name')
        self.genero = kwargs.get('genero')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
        self.lugar_nacimiento = kwargs.get('lugar_nacimiento')
        self.identificacion = kwargs.get('identificacion')
        self.imagen = kwargs.get('imagen')
        self.grupo = kwargs.get('grupo')

    def to_dict(self):
        return { 'id_usuario' : self.id_usuario,
                 'email' : self.email,
                 'password' : self.password,
                 'username' : self.username,
                 'nombre' : self.nombre,
                 'apellido' : self.apellido,
                 'genero' : self.genero,
                 'fecha_nacimiento' : self.fecha_nacimiento,
                 'lugar_nacimiento' : self.lugar_nacimiento,
                 'identificacion' : self.identificacion,
                 'imagen' : self.imagen,
                 'grupo' : self.grupo
                 }

class GrupoDTO():
    def __init__(self, *args, **kwargs):
        self.id_grupo = kwargs.get('id_grupo')
        self.grupo = kwargs.get('grupo')
        self.descripcion = kwargs.get('descripcion')

    def to_dict(self):
        return {'id_grupo' : self.id_grupo,
                'grupo' : self.grupo,
                'descripcion' : self.descripcion
                }

class RecursoDTO():
    def __init__(self, *args, **kwargs):
        self.id_recurso = kwargs.get('id_recurso')
        self.recurso = kwargs.get('recurso')
        self.descripcion = kwargs.get('descripcion')

    def to_dict(self):
        return {'id_recurso' : self.id_recurso,
                'recurso' : self.recurso,
                'descripcion' : self.descripcion
                }
