from abc import ABC, abstractmethod

from usuarios.repositorio.abstract_factory import AbstractFactory

class RolFactory(ABC):
    database = AbstractFactory.get_database()
    database.connect()

    @abstractmethod
    def insert_rol(self, rol):
        pass

    @abstractmethod
    def insert_roles(self, roles):
        pass

    @abstractmethod
    def select_rol(self, id_rol):
        pass

    @abstractmethod
    def select_all_roles(self):
        pass

    @abstractmethod
    def ubdate_rol(self, rol):
        pass

    @abstractmethod
    def delete_rol(self, id_rol):
        pass


