from flask import Flask, request, jsonify

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/')
@app.route('/home')
def home():
    return 'home'

@app.route('/usuarios', methods=['GET'])
def usuarios_GET():
    return 'get todos los usuarios'

@app.route('/usuarios', methods=['POST'])
def usuarios_POST():
    return 'post uno o varios usuarios'

@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def usuario_GET(id_usuario):
    return 'get usuario con id_usuario'

@app.route('/usuarios/login', methods=['POST'])
def usuarios_login():
    rq = request.data
    return 'login'

@app.route('/usuarios/login', methods=['POST'])
def usuarios_logout():
    return 'logout'



if __name__ == '__main__':
    app.run()
