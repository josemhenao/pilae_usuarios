from peewee import *
from usuarios.repositorio.abstract_factory import AbstractFactory

class BaseModel(Model):
    class Meta:
        database = AbstractFactory.get_database()

class Recurso(BaseModel):
    id_recurso = AutoField(primary_key=True)
    nombre = CharField(max_length=40)
    descripcion = TextField(null = True)

    def to_dic(self):
        return {'id_recurso':self.id_recurso,
                'nombre':self.id_nombre,
                'descripcion':self.descripcion
                }

class Rol(BaseModel):
    id_rol = AutoField(primary_key=True)
    nombre = CharField(max_length=40)
    descripcion = TextField(null = True)
    recursos = ManyToManyField(Recurso, backref='grupo')

    def to_dict(self):
        recursos_list = [r for r in self.recursos]
        return {'id_rol':self.id_rol,
                'nombre':self.nombre,
                'descripcion':self.descripcion,
                'recursos':[r.id_recurso for r in recursos_list]
                }

class Usuario(BaseModel):
    id_usuario = AutoField(primary_key=True)
    email = CharField(max_length=60)
    password = CharField(max_length=255)
    username = CharField(max_length=40)
    nombre = CharField(max_length=40, null=True)
    apellido = CharField(max_length=40, null=True)
    genero = CharField(max_length=20, default='Masculino')
    fecha_nacimiento = DateField()
    lugar_nacimiento = CharField(max_length=40)
    identificacion = CharField(max_length=30, null=True)
    imagen = CharField(max_length=255, null=True, default='default.png')
    rol = ForeignKeyField(Rol, null = True)

    def to_dict(self):
        return {'id_usuario':self.id_usuario,
                'email':self.email,
                'username':self.username,
                'nombre':self.nombre,
                'apellido':self.apellido,
                'genero':self.genero,
                'fecha_nacimiento':{'day':self.fecha_nacimiento.day,
                                    'month': self.fecha_nacimiento.month,
                                    'year': self.fecha_nacimiento.year,
                                    } if self.fecha_nacimiento is not None else None,
                'lugar_nacimiento':self.lugar_nacimiento,
                'identificacion':self.identificacion,
                'imagen':self.imagen,
                'rol' : self.rol.id_rol if self.rol is not None else None
                }

GrupoRecurso = Rol.recursos.get_through_model()

class Session(BaseModel):
    seesion_id = CharField(max_length=80, primary_key=True)
    session_data = CharField(max_length=255)
    expire_date = DateTimeField()
