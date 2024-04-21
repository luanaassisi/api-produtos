from pytest import fixture
from src.repositories.produtos_repository import ProdutosRepository
from src.services.produtos_service import ProdutosService

@fixture
def produtos_service():
    produtos_repo = ProdutosRepository()
    produtos_service = ProdutosService(produtos_repo)
    return produtos_service

def test_obter_todos_produtos(produtos_service):

    pagina = '2'

    resposta, status_code = produtos_service.obter_todos_produtos(pagina)

    assert resposta['paginaAtual'] == pagina
    assert resposta['totalDePaginas'] > 0
    assert len(resposta['data']) > 0
    assert status_code == 200

def test_obter_produto_especifico_none(produtos_service):

    produto_id = 'id_invalido'

    resposta, status_code = produtos_service.obter_produto_especifico(produto_id)

    assert resposta['message'] == 'Produto nao encontrado'
    assert status_code == 400

def test_obter_produto_especifico_not_none(produtos_service):

    produto_id = '5'

    resposta, status_code = produtos_service.obter_produto_especifico(produto_id)

    assert resposta['data']['id'] == produto_id
    assert status_code == 200

def test_criar_produto_sem_preco(produtos_service):
    
    dados_produto = {
        'nome': 'produto_novo'
    }

    resposta, status_code = produtos_service.criar_produto(dados_produto)

    assert resposta['message'] == 'Nome ou preco nao preenchidos'
    assert status_code == 400

def test_criar_produto_preco_invalida(produtos_service):

    dados_produto = {
        'nome': 'produto_novo',
        'preco': 'preco_invalido'
    }

    resposta, status_code = produtos_service.criar_produto(dados_produto)

    assert resposta['message'] == 'Preco precisa ser numerico'
    assert status_code == 400

def test_criar_produto_sucesso(produtos_service):

    dados_produto = {
        'nome': 'novo_produto',
        'preco': '9000.00'
    }

    resposta, status_code = produtos_service.criar_produto(dados_produto)

    assert isinstance(resposta['data'], dict)
    assert status_code == 200

def test_remover_produto_none(produtos_service):

    produto_id = 'id_invalido'

    resposta, status_code = produtos_service.remover_produto(produto_id)

    assert resposta['message'] == 'produto nao encontrado'
    assert status_code == 400

def test_remover_produto_sucesso(produtos_service):

    produto_id = '2'

    resposta, status_code = produtos_service.remover_produto(produto_id)

    assert resposta['message'] == f'Produto {produto_id} removido com sucesso'
    assert status_code == 200

def test_alterar_produto_preco_invalido(produtos_service):

    produto_id = '1'

    dados_produto = {
        'nome': 'produto_alterado'
    }
    resposta, status_code = produtos_service.alterar_produto(produto_id, dados_produto)

    assert resposta['message'] == 'Nome ou preco nao preenchidos'
    status_code == 400

def test_alterar_produto_nao_encontrado(produtos_service):

    produto_id = 'id_invalido'

    dados_produto = {
        'nome': 'produto_alterado',
        'preco': '38.60'
    }
    resposta, status_code = produtos_service.alterar_produto(produto_id, dados_produto)

    assert resposta['message'] == 'Produto nao encontrado'
    assert status_code == 400

def test_alterar_produto_sucesso(produtos_service):

    produto_id = '2'

    dados_produto = {
        'nome': 'produto_alterado',
        'preco': '38.60'
    }

    resposta, status_code = produtos_service.alterar_produto(produto_id, dados_produto)

    assert resposta['message'] == f'Produto {produto_id} alterado com sucesso'
    assert status_code == 200