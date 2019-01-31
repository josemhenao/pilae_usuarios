from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase
from abc import ABC, abstractmethod
from settings import db_config


class AbstractFactory(ABC):
    database = None

    @abstractmethod
    def get_database():
        '''
            returns the database created according to the engine defined in the settings file
            :return: database
        '''
        database = None
        engine = db_config.get('engine')
        db = db_config.get('database')

        db_access = {'host' : db_config.get('host'),
                    'user' : db_config.get('user'),
                    'password' : db_config.get('password')
                    }

        if engine.lower() == 'mysql':
            database = MySQLDatabase(database=db,**db_access)
        elif engine.lower() == 'postgresql':
            database = PostgresqlDatabase(database=db, **db_access)
        elif engine.lower() == 'sqlite':
            database = SqliteDatabase(database=db, **db_access)

        return database