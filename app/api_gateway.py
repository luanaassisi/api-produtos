import requests
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token


app_gtw = Flask(__name__)

app_gtw.config['JWT_SECRET_KEY'] = 'segredo' 
jwt = JWTManager(app_gtw)

PRODUTO_SERVICE_URL = "http://localhost:5000"

@app_gtw.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

   
    if username == 'admin' and password == 'admin':

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app_gtw.route('/produtos', methods=['GET'])
@jwt_required()
def gtw_listar_produtos():
    parametros = request.args
    resposta = requests.get(f"{PRODUTO_SERVICE_URL}/produtos", params=parametros)
    return jsonify(resposta.json()), resposta.status_code


@app_gtw.route('/produtos/<int:produto_id>', methods=['GET'])
@jwt_required()
def gtw_obter_produtos_especifico(produto_id):
    resposta = requests.get(f"{PRODUTO_SERVICE_URL}/produtos/{produto_id}")
    return jsonify(resposta.json()), resposta.status_code


@app_gtw.route('/produtos', methods=['POST'])
@jwt_required()
def gtw_criar_produto():
    dados_produto = request.get_json()
    resposta = requests.post(f"{PRODUTO_SERVICE_URL}/produtos", json=dados_produto)
    return jsonify(resposta.json()), resposta.status_code


@app_gtw.route('/produtos/<int:produto_id>', methods=['PUT'])
@jwt_required()
def gtw_alterar_produto(produto_id):
    dados_produto = request.get_json()
    resposta = requests.put(f"{PRODUTO_SERVICE_URL}/produtos/{produto_id}", json=dados_produto)
    return jsonify(resposta.json()), resposta.status_code

@app_gtw.route('/produtos/<int:produto_id>', methods=['DELETE'])
@jwt_required()
def gtw_remover_produto(produto_id):
    resposta = requests.delete(f"{PRODUTO_SERVICE_URL}/produtos/{produto_id}")
    return jsonify(resposta.json()), resposta.status_code


if __name__ == '__main__':
    app_gtw.run(debug=True, port=5001)
