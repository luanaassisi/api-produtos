from random import uniform


class ProdutosRepository:

    def __init__(self):
        lista_produtos = []
        for i in range(1000):
            lista_produtos.append(
                {"id": str(i), 
                 "nome": f"produto {i}", 
                 "preco": str(round(uniform(0,9), 2))})

        self.produtos = lista_produtos

    def obter_todos_produtos(self, offset, qtd_linhas_por_pagina):
        total_de_produtos = len(self.produtos)
        return self.produtos[offset:offset + qtd_linhas_por_pagina], total_de_produtos
        
    def obter_produto_especifico(self, produto_id: str):
        for produto in self.produtos:
            if produto['id'] == produto_id:
                return produto
            
    def criar_produto(self, dados_produtos: dict):
        lista_de_ids = []
        for produto in self.produtos:
            lista_de_ids.append(int(produto['id']))
        
        ultimo_id = max(lista_de_ids)
        novo_id = ultimo_id + 1

        novo_produto = {
            'id': str(novo_id),
            'nome': str(dados_produtos['nome']),
            'preco': str(dados_produtos['preco'])
        }

        self.produtos.append(novo_produto)
        print(self.produtos)

        return novo_produto

    def alterar_produto(self, produto_id: str, dados_produto: dict):
        for produto in self.produtos:
            if produto['id'] == produto_id:
                produto['nome'] = dados_produto['nome']
                produto['preco'] = dados_produto['preco']

                return produto
    
    def remover_produto(self, produto_id: str):
        for produto in self.produtos:
            if produto['id'] == produto_id:
                self.produtos.remove(produto)
                
                return produto