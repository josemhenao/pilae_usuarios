from usuarios.repositorio.abstractfactory import AbstractFactory
from usuarios.repositorio.models import Recurso, Grupo, Usuario

# Run this script when you have modified or created a Repository Model.
# Make sure there are no tables in the database that could interfere with
# the creation of the new tables
database = AbstractFactory.get_database()
database.connect()

database.create_tables([Recurso,Grupo,Usuario])

