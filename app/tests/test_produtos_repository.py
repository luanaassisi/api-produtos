from pytest import fixture
from src.repositories.produtos_repository import ProdutosRepository

@fixture
def produtos_repo():
    produtos_repo = ProdutosRepository()
    return produtos_repo

def test_obter_todos_produtos(produtos_repo):

    lista_de_produtos, total_de_produtos = produtos_repo.obter_todos_produtos(0, 25)
    primeiro_produto = lista_de_produtos[0]

    assert len(lista_de_produtos) == 25 
    assert "id" in primeiro_produto
    assert "nome" in primeiro_produto
    assert "preco" in primeiro_produto
    assert isinstance(total_de_produtos, int)

def test_obter_produto_especifico_not_none(produtos_repo):

    produto = produtos_repo.obter_produto_especifico("2")
    
    assert produto is not None
    assert produto["id"] == '2'
    assert "nome" in produto
    assert "preco" in produto

def test_obter_produto_especifico_none(produtos_repo):

    produto = produtos_repo.obter_produto_especifico('id_invalido')

    assert produto is None

def test_criar_produto(produtos_repo):

    dados_produto = {
        'nome': 'Ps5',
        'preco': '4000.00'
    }

    novo_produto = produtos_repo.criar_produto(dados_produto)

    assert 'id' in novo_produto
    assert novo_produto['nome'] == dados_produto['nome']
    assert novo_produto['preco'] == dados_produto['preco']
    assert novo_produto in produtos_repo.produtos

def test_alterar_produto_not_none(produtos_repo):
    
    produto_id = '5'
    dados_produto = {
        'nome': 'produto_alterado',
        'preco': '5000.00'
    }

    produto = produtos_repo.alterar_produto(produto_id, dados_produto)

    assert produto['id'] == produto_id
    assert produto['nome'] == dados_produto['nome']
    assert produto['preco'] == dados_produto['preco']
    assert produto in produtos_repo.produtos

def test_alterar_produto_none(produtos_repo):
    
    produto_id = 'id_invalido'
    dados_produto = {
        'nome': 'produto_alterado',
        'preco': '5000.00'
    }

    produto = produtos_repo.alterar_produto(produto_id, dados_produto)

    assert produto is None

def test_remover_produto(produtos_repo):
    produto = produtos_repo.remover_produto('6')

    assert produto not in produtos_repo.produtos






