import requests
from flask import Flask, jsonify, request



app = Flask(__name__)

PRODUTO_SERVICE_URL = "http://localhost:5000"


@app.route('/produtos', methods=['GET'])
def gtw_listar_produtos():
    parametros = request.args
    resposta = requests.get(f"{PRODUTO_SERVICE_URL}/produtos", params=parametros)
    return jsonify(resposta.json()), resposta.status_code


@app.route('/produtos/<int:produto_id>', methods=['GET'])
def gtw_obter_produtos_especifico(produto_id):
    resposta = requests.get(f"{PRODUTO_SERVICE_URL}/produtos/{produto_id}")
    return jsonify(resposta.json()), resposta.status_code


@app.route('/produtos', methods=['POST'])
def gtw_criar_produto():
    dados_produto = request.get_json()
    resposta = requests.post(f"{PRODUTO_SERVICE_URL}/produtos", json=dados_produto)
    return jsonify(resposta.json()), resposta.status_code


@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def gtw_alterar_produto(produto_id):
    dados_produto = request.get_json()
    resposta = requests.put(f"{PRODUTO_SERVICE_URL}/produtos/{produto_id}", json=dados_produto)
    return jsonify(resposta.json()), resposta.status_code

@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def gtw_remover_produto(produto_id):
    resposta = requests.delete(f"{PRODUTO_SERVICE_URL}/produtos/{produto_id}")
    return jsonify(resposta.json()), resposta.status_code


if __name__ == '__main__':
    app.run(debug=True, port=5001)
