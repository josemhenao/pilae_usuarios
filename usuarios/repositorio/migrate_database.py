from usuarios.repositorio.abstract_factory import AbstractFactory
from usuarios.repositorio.models import Recurso, Rol, Usuario, GrupoRecurso
from peewee import IntegrityError


# Run this script when you have modified or created a Repository Model.
# Make sure there are no tables in the database that could interfere with
# the creation of the new tables. Define DBMS configurations in settings file

# database = AbstractFactory.get_database()
# database.connect()
#
# database.create_tables([Recurso, Rol, Usuario, GrupoRecurso])


# try:
#     recurso_1 = Recurso.create(id_recurso = 1,
#                            nombre = 'puede_crear_usuarios',
#                            descripcion = 'descripcion recurso_1'
#                            )
# except IntegrityError:
#     print(IntegrityError)
#
# try:
#     recurso_2 = Recurso.create(id_recurso=2,
#                                nombre='puede_crear_equipos',
#                                descripcion='descripcion recurso_2'
#                                )
# except IntegrityError:
#     print(IntegrityError)
#
# try:
#     recurso_3 = Recurso.create(id_recurso=3,
#                                nombre='puede_crear_torneos',
#                                descripcion='descripcion recurso_3'
#                                )
# except IntegrityError:
#     print(IntegrityError)
#
# try:
#     rol_1 = Rol.create(id_rol=1,
#                        nombre='administrador',
#                        descripcion='descripcion rol_1'
#                        )
# except IntegrityError:
#     print(IntegrityError)
#
# try:
#     rol_JSON = {
#         'id_rol':2,
#         'nombre':'jugador',
#         'descripcion':'descripcion rol_2 de jugador'
#     }
#
#     rol_2 = Rol.create(**rol_JSON)
# except IntegrityError:
#     print(IntegrityError)

# try:
#     josemJSON = {'username':'josemhenao123',
#                  'email':'josem.henao@gmail.com',
#                  'password':'josemhenao123123',
#                  'nombre':'José Miguel',
#                  'apellido':'Henao Cardona',
#                  'rol': Rol.get_by_id(1),
#                  'genero':'Masculino',
#                  'fecha_nacimiento': date(1994,6,22),
#                  'lugar_nacimiento':'Medellín'
#                  }
#
#     user_4 = Usuario(**josemJSON)
#     user_4.save()
#     print(user_4)
#
# except IntegrityError:
#     print(IntegrityError)

#user = Usuario.get(id_usuario = 13)
#print(user.to_dict())

usuarios = Usuario.select()
for u in usuarios:
    print(u.to_dict())


#rol = Rol.get()


