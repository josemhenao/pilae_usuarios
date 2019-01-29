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