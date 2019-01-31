
def get_usuario(id_usuario):
    return {'message':'llamando a get_usuario()',
            'other':'Have a nice day!'
            }

def get_all_usuarios():
    return {'message':'llamando a get_all_usuarios()',
            'other':'Have a nice day dude!,'
            }

def post_usuario(usuarios):
    print(usuarios)
    return {'message':'llamando a post_usuario()',
            'other':'Have a nice day dude!,'
            }
