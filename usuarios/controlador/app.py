from flask import Flask, request, jsonify, g
from usuarios.dominio.usuario_dominio import UsuarioDominio
from usuarios.controlador.usuario_controlador import UsuarioControlador
app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/')
@app.route('/home')
def home_GET(*args,**kwargs):
    print(request.headers.get('Authorization'))
    print(request.get_json())
    return jsonify({'message':'home!, use a valid url...'})

@app.route('/usuarios', methods=['GET'])
def usuarios_GET():
    return jsonify(UsuarioDominio.read_all_usuarios())

@app.route('/usuarios', methods=['POST'])
def usuarios_POST():
    data = request.get_json() or {}
    if type(data) is not dict:
        return jsonify({'message':'Data sent as parameters does not have the JSON structure'})
    elif len(data) == 0:
        return jsonify({'message': 'No user data has been sent'})
    # elif len(data) == 1:
    #     return jsonify(UsuarioDominio.create_usuario(data.get('usuario_1')))
    # elif len(data) > 1:
    #     return jsonify(UsuarioDominio.create_usuarios(data))
    elif len(data) >= 1:
        for e in data:
            if UsuarioControlador.is_data_type_validate(data[e]):
                return jsonify({'message':'Some data types are not correct'})
        return jsonify(UsuarioDominio.create_usuario(data))
    else:
        return jsonify({'message':'The request could not be interpreted'})

@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def usuario_GET(id_usuario):
    return jsonify(UsuarioDominio.read_usuario(id_usuario))

@app.route('/usuarios/login', methods=['POST'])
def usuarios_login():
    rq = request.data
    return 'login'

@app.route('/usuarios/logout', methods=['POST'])
def usuarios_logout():
    return 'logout'



if __name__ == '__main__':
    app.run()
