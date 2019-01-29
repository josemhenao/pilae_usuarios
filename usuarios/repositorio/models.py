from peewee import *

from usuarios.repositorio.abstract_factory import Abstract_Factory


class BaseModel(Model):
    class Meta:
        database = Abstract_Factory.get_database()

class Recurso(BaseModel):
    id_recurso = AutoField(primary_key=True)
    nombre = CharField(max_length=40)
    descripcion = TextField(null = True)

class Grupo(BaseModel):
    id_grupo = AutoField(primary_key=True)
    nombre = CharField(max_length=40)
    descripcion = TextField(null = True)
    recursos = ManyToManyField(Recurso, on_delete='cascade')

class Usuario(BaseModel):
    id_usuario = AutoField(primary_key=True)
    email = CharField(max_length=60)
    password = CharField(max_length=255)
    username = CharField(max_length=40)
    nombre = CharField(max_length=40, null=True)
    apellido = CharField(max_length=40, null=True)
    genero = CharField(max_length=20)
    fecha_nacimiento = DateField()
    lugar_nacimiento = CharField(max_length=40)
    identificacion = CharField(max_length=30, null=True)
    imagen = CharField(max_length=255, null=True, default='default.png')
    grupo = ForeignKeyField(Grupo, null = True)
