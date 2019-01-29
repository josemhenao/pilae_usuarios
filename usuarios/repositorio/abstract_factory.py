from settings import db_config
from peewee import MySQLDatabase, PostgresqlDatabase
from abc import ABC, abstractmethod

class Abstract_Factory(ABC):
    def __init__(self, db_config):
        self.__db_config = db_config
        self.__database = None
        super().__init__()


    @abstractmethod
    def get_database(self):
        pass

    @abstractmethod
    def __init_database(self):
        engine = self.__db_config.get('engine')
        host = self.__db_config.get('host')
        user = self.__db_config.get('user')
        password = self.__db_config.get('password')
        db = self.__db_config.get('database')

        if engine.lower() == 'mysql':
            self.__database = MySQLDatabase(host=host,
                                            user = user,
                                            password = password,
                                            database=db
                                            )
        elif engine.lower() == 'postgresql':
            self.__database = PostgresqlDatabase(host=host,
                                                 user = user,
                                                 password = password,
                                                 database=db
                                                 )
        elif engine.lower() == 'sqlite':
            self.__database = PostgresqlDatabase(host=host,
                                                 user = user,
                                                 password = password,
                                                 database=db
                                                 )



