import math
from src.repositories.produtos_repository import ProdutosRepository


class ProdutosService:

    def __init__(self, 
                 produtos_repo: ProdutosRepository):
        self.produtos_repo = produtos_repo


    def obter_todos_produtos(self, pagina: str):
        qtd_linhas_por_pagina = 25
        offset = (int(pagina) - 1) * qtd_linhas_por_pagina

        produtos, total_de_produtos = self.produtos_repo.obter_todos_produtos(
            offset, qtd_linhas_por_pagina)
        
        total_de_paginas = math.ceil(total_de_produtos / qtd_linhas_por_pagina)

        resposta = {
            'data': produtos, 
            'totalDePaginas': total_de_paginas,
            'paginaAtual': pagina
        }

        return resposta, 200
    
    def obter_produto_especifico(self, produto_id: str):
        produto_retornado = self.produtos_repo.obter_produto_especifico(
            produto_id)
        
        if produto_retornado is None:

            resposta = {
                'message': 'Produto nao encontrado'
            }

            return resposta, 400
        
        resposta = {
            'data': produto_retornado
        }
        return resposta, 200
    
    def criar_produto(self, dados_produto: dict):
        if 'nome' not in dados_produto or 'preco' not in dados_produto:
            resposta = {
                'message': 'Nome ou preco nao preenchidos'
            }
            return resposta, 400
        
        preco = str(dados_produto['preco'])
        dados_produto['preco'] = preco
        
        if not preco.replace(".", "").isnumeric():
            resposta = {
                'message': 'Preco precisa ser numerico'
            }
            return resposta, 400

        produto_criado = self.produtos_repo.criar_produto(dados_produto)
        
        resposta = {
            'data': produto_criado
        }
        return resposta, 200
    
    def remover_produto(self, produto_id: str):
        produto_removido = self.produtos_repo.remover_produto(
            produto_id)
        
        if produto_removido is None:
            resposta = {
                'message': 'produto nao encontrado'
            }
            return resposta, 400
        
        resposta = {
            'message': f'Produto {produto_id} removido com sucesso'
        }
        return resposta, 200
    
    def alterar_produto(self, produto_id: str, dados_produto: dict):
        if 'nome' not in dados_produto or 'preco' not in dados_produto:
            resposta = {
                'message': 'Nome ou preco nao preenchidos'
            }
            return resposta, 400

        dados_produto['preco'] = str(dados_produto['preco'])

        produto_alterado = self.produtos_repo.alterar_produto(
            produto_id, dados_produto)
        
        if produto_alterado is None:
            resposta = {
                'message': 'Produto nao encontrado'
            }
            return resposta, 400
        
        resposta = {
            'message': f'Produto {produto_id} alterado com sucesso'
        }
        return resposta, 200

        



    
    

