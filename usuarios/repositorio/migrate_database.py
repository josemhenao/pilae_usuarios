from usuarios.repositorio.abstract_factory import Abstract_Factory
from usuarios.repositorio.models import Recurso, Grupo, Usuario

# Run this script when you have modified or created a Repository Model.
# Make sure there are no tables in the database that could interfere with
# the creation of the new tables
database = Abstract_Factory.get_database()
database.connect()

database.create_tables([Recurso,Grupo,Usuario])