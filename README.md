## Api-produtos

    Este projeto consiste em um sistema de gerenciamento de produtos, desenvolvido em Python utilizando Flask para criação de uma API REST. Ele inclui funcionalidades básicas para listar, criar, atualizar e excluir produtos expostas através de uma simulação de api-gateway com autenticação JWT.

### Passo a passo:

    1. Clonar repositório: git clone https://github.com/luanaassisi/api-produtos.git
    2. Instalação de requisitos: pip install -r requirements.txt
    3. Rodar aplicação: python app/main.py 
    4. Rodar api gateway: python app/api_gateway.py

#### Exemplo de uso da API:

    Base url : "http://localhost:5001/"

    Obs: Todos os endpoints são protegidos através de um token que deve ser inserido como Bearer token que pode ser adquirido no endpoint abaixo:

    /login
        POST
            body: {
                    "username": "admin",
                    "password": "admin"
                }
            response: {
                        "access_token": "token"
                    }


    /produtos
        GET:
            description: Listar todos os produtos
            queryString: {
                'pagina': str
            }
            response: {
                        "data": [
                            {
                                "id": "0",
                                "nome": "produto 0",
                                "preco": "6.74"
                            },
                            {
                                "id": "1",
                                "nome": "produto 1",
                                "preco": "2.49"
                            }
                        ],
                        "paginaAtual": 1,
                        "totalDePaginas": 40
                    }
        POST:
            description: Criar novo produto
            body:{
                    "nome": "ps5",
                    "preco": "5000.00"
                }
            response:{
                        "data": {
                            "id": "1001",
                            "nome": "ps5",
                            "preco": "5000.00"
                        }
                    }


    /produtos/{produtoId}
        GET:
            description: Consultar produto especifico
            response:{
                        "message": "Produto {produtoId} alterado com sucesso"
                    }

        PUT:
            description: Alterar produto
            body:{
                    "nome": "novo_nome",
                    "preco": "5000.00"
                }
            response:{
                        "message": "Produto {produtoId} alterado com sucesso"
                    }

        DELETE:
            description: Remove produto especifico
            response:{
                        "message": "Produto {produtoId} removido com sucesso"
                    }

