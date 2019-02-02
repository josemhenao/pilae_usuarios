from peewee import MySQLDatabase

# This is the DataBase Configuration, we are using peewee as a Python ORM, you can choose
# MySQL, Sqlite or Postgre as a Database Engine (Sqlite is the default one)
db_config = {
    'engine':'mysql',
    'host':'localhost',
    'user':'root',
    'password':'admin123*',
    'database':'pilae_usuarios'
}

# Atributos requeridos (no nulos) para que los datos de una peticion POST a usuarios sea correcta
REQUIRED_USUARIO = {
    'id_usuario':True,
    'email':True,
    'password':False,
    'username':True,
    'nombre':False,
    'apellido':False,
    'genero':True,
    'fecha_nacimiento':True,
    'lugar_nacimiento':True,
    'identificacion':False,
    'imagen':False,
    'rol_id': False
}