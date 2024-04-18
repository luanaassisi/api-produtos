from flask import Flask, request
from repositories.produtos_repository import ProdutosRepository
from services.produtos_service import ProdutosService

app = Flask(__name__)
produtos_repository = ProdutosRepository()
produtos_service = ProdutosService(produtos_repository)

@app.route('/produtos', methods=['GET'])
def listar_produtos():

    pagina = request.args.get('pagina', 1)
    resposta = produtos_service.obter_todos_produtos(pagina)

    return resposta

@app.route('/produtos/<produto_id>', methods=['GET'])
def obter_produto_especifico(produto_id):
    resposta = produtos_service.obter_produto_especifico(
        produto_id)

    return resposta

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados_produto = request.get_json()
    resposta = produtos_service.criar_produto(dados_produto)

    return resposta

@app.route('/produtos/<produto_id>', methods=['PUT'])
def alterar_produto(produto_id):
    dados_produto = request.get_json()
    resposta = produtos_service.alterar_produto(produto_id, dados_produto)

    return resposta 

@app.route('/produtos/<produto_id>', methods=['DELETE'])
def remover_produto(produto_id):
    resposta = produtos_service.remover_produto(produto_id)

    return resposta



    
if __name__ == '__main__':
    app.run(port=5000)