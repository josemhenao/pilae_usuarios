import functools

from usuarios.dominio.auth_dominio import AuthDominio

def login_required():
    @functools.wrap
    def wrapper(f):
        # Create procces to validate login
        return None
    return wrapper

