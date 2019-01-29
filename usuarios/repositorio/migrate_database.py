from usuarios.repositorio.abstract_factory import Database_conection
from usuarios.repositorio.models import Recurso, Grupo, Usuario

database = Database_conection()
database.connect()

database.create_tables([Recurso,Grupo,Usuario])

# josem = Usuario.create(nombre = 'José Miguel',
#                        apellido = 'Henao',
#                        genero = 'Masculino',
#                        fecha_nacimiento = date(1994, 6, 22),
#                        lugar_nacimiento = 'Rionegro'
#                        )
#
# juanjose = Usuario.create(nombre = 'Juan José',
#                        apellido = 'Giraldo',
#                        genero = 'Masculino',
#                        fecha_nacimiento = date(1997, 1, 15),
#                        lugar_nacimiento = 'Rionegro'
#                        )


qr = Usuario.get(nombre='José Miguel')

print(qr)